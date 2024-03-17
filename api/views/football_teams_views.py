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
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_http_methods

# Get all football teams 
class FootballTeamsView(generics.ListAPIView):
    queryset = FootballTeam.objects.all()
    serializer_class = FootballTeamSerializer

# Get a specific team
class SingleFootballTeamView(APIView):
    def get(self, request, id, format=None):
        try:
            team = FootballTeam.objects.get(id=id)
            serializer = FootballTeamSerializer(team)
            return Response(serializer.data)
        except FootballTeam.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)