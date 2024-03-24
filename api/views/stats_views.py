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
from django.db.models import F, FloatField
from django.db.models.functions import Cast
from rest_framework.views import APIView
from rest_framework.response import Response
from api.utils import GetDefaultScoringParams, calc_game_f_points

# Get all player stats for a given season
class GetSeasonStatsListView(APIView):
    serializer_class = PlayerSeasonStatsSerializer

    def get(self, request, year, format=None):
        if year is not None:
            # Filter the queryset based on the provided year
            queryset = PlayerSeasonStats.objects.filter(year=year).all()
        else:
            # Handle the case where no year is provided
            queryset = PlayerSeasonStats.objects.none()

        # Serialize and return the filtered queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# Top performers - 1 of each position
class GetTopPerformers(APIView):
    def get(self, request, *args, **kwargs):
        scoring_params = GetDefaultScoringParams()

        annotated_stats = PlayerSeasonStats.objects.filter(year='2024').select_related('player').annotate(
            fantasy_points=Cast(0, FloatField()) +
            F('passing_yards') * scoring_params['passing_yards'] +
            F('passing_tds') * scoring_params['passing_tds'] +

            F('rushing_yards') * scoring_params['rushing_yards'] +
            F('rushing_tds') * scoring_params['rushing_tds'] +

            F('receptions') * scoring_params['receptions'] +
            F('receiving_yards') * scoring_params['receiving_yards'] +
            F('receiving_tds') * scoring_params['receiving_tds'] +

            F('fgm0_19') * scoring_params['fgm0_19'] +
            F('fgm20_39') * scoring_params['fgm20_39'] +
            F('fgm40_49') * scoring_params['fgm40_49'] +
            F('fgm50_plus') * scoring_params['fgm50_plus'] +
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


# Search for Stats Page
class StatsSearchView(APIView):
    serializer = PlayerSeasonStatsSerializer

    def post(self, request, format=None):
        # Extract filters from request data
        selected_positions = request.data.get('selectedPositions', [])
        selected_teams = request.data.get('selectedTeams', [])
        selected_seasons = request.data.get('selectedSeasons', [])
        
        # Building the queryset
        queryset = PlayerSeasonStats.objects.all()
        
        if selected_positions:
            queryset = queryset.filter(player__position__in=selected_positions)
        if selected_teams:
            queryset = queryset.filter(player__team_id__in=selected_teams)
        if selected_seasons:
            queryset = queryset.filter(year__in=selected_seasons)
        
        # Serialize and return the filtered queryset
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data)
    

class RankingsView(APIView):
    def get(self, request):
        players = FootballPlayer.objects.all()

        # Generate a random float for each player and add it to the player's instance
        for player in players:
            player_game_logs = PlayerGameLog.objects.filter(player=player).order_by('-year','-week')[:4]
            
            # Calculate points (average of last 4 games)
            total_points_last_4 = 0.0
            for game in player_game_logs:
                setattr(game, 'points', calc_game_f_points(game, GetDefaultScoringParams()))
                total_points_last_4 += game.points
            setattr(player, 'projected_points', round(total_points_last_4/4,2))

        # Sort players by 'projected_points' in descending order
        sorted_players = sorted(players, key=lambda x: x.projected_points, reverse=True)

        # Add 'position' based on order in sorted list
        for position, player in enumerate(sorted_players, start=1):
            setattr(player, 'ranking', position)

        # Since we've manually added attributes to the instances, ensure your serializer can handle them
        # You might need to adjust FootballPlayerSummarySerializer to include 'projected_points' and 'position'
        serializer = FootballPlayerSummarySerializer(sorted_players, many=True)
        return Response(serializer.data)


# Get all player game logs for a given season
class GetPlayerSeasonGameLogsView(APIView):
    serializer_class = PlayerGameLogSerializer

    def get(self, request, player_id, year, format=None):
        if year is not None:
            # Filter the queryset based on the provided year
            queryset = PlayerGameLog.objects.filter(player__id=player_id, year=year).all()
        else:
            # Handle the case where no year is provided
            queryset = PlayerGameLog.objects.none()

        # Serialize and return the filtered queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
# Get Recent Game Logs For Player
class GetPlayerRecentGameLogsView(APIView):
    serializer_class = PlayerGameLogSerializer

    def get(self, request, player_id, format=None):
        if player_id is not None:
            # Filter the queryset based on the provided year
            queryset = PlayerGameLog.objects.filter(player__id=player_id).order_by('-year', '-week')[:4]
        else:
            # Handle the case where no year is provided
            queryset = PlayerGameLog.objects.none()

        # Serialize and return the filtered queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)