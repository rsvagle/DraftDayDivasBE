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

# Get all player stats for a given season
# Pass in year
class GetSeasonStatsListView(APIView):
    serializer_class = PlayerSeasonStatsSerializer

    def get(self, request, year, format=None):
        if year is not None:
            # Filter the queryset based on the provided year
            queryset = PlayerSeasonStats.objects.filter(year=year).all()
        else:
            # Optionally, handle the case where no year is provided, such as returning all objects or none
            queryset = PlayerSeasonStats.objects.none()  # Example: Return an empty queryset

        # Serialize and return the filtered queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)