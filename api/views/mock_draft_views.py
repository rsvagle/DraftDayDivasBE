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
        print("perform create worked!")
        # Here we explicitly set defaults.
        print(serializer)

        serializer.save(teams_joined=0, has_started=False, has_finished=False)

    # Enforce authentication for creating a new draft.
    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Get the serializer instance with the incoming data
        serializer = self.get_serializer(data=request.data)
        # Validate the data; if invalid, an error response is returned automatically.
        serializer.is_valid(raise_exception=True)
        # Call perform_create to save the instance with defaults
        self.perform_create(serializer)
        # Prepare headers and response as usual
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FantasyDraftJoinView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Only authenticated users can join a draft

    def post(self, request, format=None):
        print("hit view")
        # Extract data from request
        draft_id = request.data.get('draft_id')
        team_name = request.data.get('team_name')
        draft_position = request.data.get('draft_position')

        print(request.data)
        print(draft_id)
        print(team_name)
        print(draft_position)

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