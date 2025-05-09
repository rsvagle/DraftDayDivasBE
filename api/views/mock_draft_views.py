from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.http import require_http_methods

# All Drafted Teams ** Needs updating to base on user
class DraftedTeamView(generics.ListAPIView):
    queryset = DraftedTeam.objects.all()
    serializer_class = DraftedTeamSerializer


class FantasyDraftListCreateView(generics.ListCreateAPIView):
    serializer_class = FantasyDraftSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    # Return AllowAny for GET requests, and IsAuthenticated for others.
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # GET: Only list drafts that haven't started.
    def get_queryset(self):
        return FantasyDraft.objects.filter(has_started=False)

    # POST: Create a new FantasyDraft object with default fields.
    def perform_create(self, serializer):
        # Create and save the draft
        draft = serializer.save()
        
        # Return the draft object which will be serialized and sent as the response
        return draft

    # Enforce authentication for creating a new draft.
    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if FantasyDraft.objects.filter(has_started=False).count() > 4:
            return Response(
                {"error": "Too many drafts exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Extract data from the request
        data = request.data.get('data')

        draft_data = {
            'number_teams': data.get('num_teams', 10),
            'teams_joined': 0,  # We'll update this after creating the team
            'has_started': False,
            'has_finished': False,
            'current_pick': 0,
        }

        # Get the serializer instance with the incoming data
        serializer = self.get_serializer(data=draft_data)

        # Validate the data; if invalid, an error response is returned automatically.
        serializer.is_valid(raise_exception=True)
        
        # Call perform_create to save the instance with defaults
        draft = self.perform_create(serializer)

        # Create the team associated with this draft and the current user
        team = FantasyDraftTeam.objects.create(
            draft=draft,
            user=self.request.user,
            team_name=data.get('team_name'),
            draft_position=data.get('draft_position')
        )

        # Prepare headers and response as usual
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FantasyDraftJoinView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Only authenticated users can join a draft

    def post(self, request, format=None):
        # Extract data from request
        draft_id = request.data.get('draft_id')
        team_name = request.data.get('team_name')
        draft_position = request.data.get('draft_position')

        # Validate that all fields are present
        if not draft_id or not team_name or draft_position is None:
            return Response(
                {"error": "Missing required fields"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Fetch the draft instance (return 404 if not found)
        draft_instance = get_object_or_404(FantasyDraft, id=draft_id)

        # Ensure the draft has not started yet
        if draft_instance.has_started:
            return Response(
                {"error": "You cannot join a draft that has already started"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the draft position is already taken
        if FantasyDraftTeam.objects.filter(draft=draft_instance, draft_position=draft_position).exists():
            return Response(
                {"error": "Draft position is already taken"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # User already joined this draft
        if FantasyDraftTeam.objects.filter(draft=draft_instance, user=request.user.id).exists():
            return Response(
                {"error": "You've already joined this draft!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create the team instance
        team_data = {
            "user": request.user.id,  # Use user ID for serialization
            "draft": draft_instance.id,
            "team_name": team_name,
            "draft_position": draft_position,
        }
        team_serializer = FantasyDraftTeamSerializer(data=team_data)

        if team_serializer.is_valid():
            team_serializer.save()
            return Response(team_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyJoinedDraftsView(generics.ListAPIView):
    serializer_class = FantasyDraftSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Only authenticated users can see their drafts

    def get_queryset(self):
        # Get all draft IDs where the current user has a team
        user_draft_ids = FantasyDraftTeam.objects.filter(
            user=self.request.user
        ).values_list('draft_id', flat=True)
        
        # Return all drafts that match these IDs
        return FantasyDraft.objects.filter(id__in=user_draft_ids)