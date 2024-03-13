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

from django.db.models import F, FloatField
from django.db.models.functions import Cast
from rest_framework.views import APIView
from rest_framework.response import Response
from api.utils import GetDefaultScoringParams

class GetTopPerformers(APIView):
    def get(self, request, *args, **kwargs):
        scoring_params = GetDefaultScoringParams()

        annotated_stats = PlayerSeasonStats.objects.select_related('player').annotate(
            fantasy_points=Cast(0, FloatField()) +
            F('passing_yards') * scoring_params['passing_yards'] +
            F('passing_tds') * scoring_params['passing_tds'] +

            F('rushing_yards') * scoring_params['rushing_yards'] +
            F('rushing_tds') * scoring_params['rushing_tds'] +

            F('receptions') * scoring_params['receptions'] +
            F('receiving_yards') * scoring_params['receiving_yards'] +
            F('receiving_tds') * scoring_params['receiving_tds'] +

            F('fgm') * scoring_params['fgm'] +
            F('xpm') * scoring_params['xpm']
        ).order_by('-fantasy_points')

        positions = ['QB', 'RB', 'WR', 'TE', 'K']
        top_performers_data = {}
        for position in positions:
            top_performer = annotated_stats.filter(player__position=position).first()
            if top_performer:
                # Serialize the player associated with the top_performer's stats
                serializer = FootballPlayerSummarySerializer(top_performer.player, context={'request': request})
                top_performers_data[position] = serializer.data

        return Response(top_performers_data)

