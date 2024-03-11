from rest_framework import serializers
from django.contrib.auth.models import User

from .models import DraftedTeam, FootballPlayer, FootballTeam, InjuryReportArticle, PlayerSeasonStats
from .models import NewsArticle

class DraftedTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftedTeam
        fields = ['id', 'userID', 'teamName', 'created_at']

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'author', 'title', 'description', 'article_content', 'image_url', 'created_at']

class InjuryReportArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjuryReportArticle
        fields = ['id', 'author', 'player_id', 'title', 'description', 'article_content', 'image_url', 'created_at']

class FootballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballTeam
        fields = '__all__'

class FootballPlayerSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    season_stats_for_season = serializers.SerializerMethodField()  # Renamed to reflect dynamic season functionality

    class Meta:
        model = FootballPlayer
        fields = '__all__'
    
    def get_team(self, obj):
        if self.context.get('include_team', False):
            serializer = FootballTeamSerializer(obj.team)
            return serializer.data
        else:
            return obj.team_id

    def get_season_stats_for_season(self, obj):
        # Retrieve the season value from the context
        season = self.context.get('season', None)
        if season:
            # Fetch the season stats for the player for the specified season
            season_stats = obj.season_stats.filter(year=season).order_by('year').first()
            if season_stats:
                serializer = PlayerSeasonStatsSerializer(season_stats)
                return serializer.data
        return None

        
class FootballPlayerSummarySerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    season_stats = serializers.SerializerMethodField()  # Renamed to reflect dynamic season functionality

    class Meta:
        model = FootballPlayer
        fields = '__all__'
    
    def get_team(self, obj):
        if self.context.get('include_team', False):
            serializer = FootballTeamSerializer(obj.team)
            return serializer.data
        else:
            return obj.team_id

    def get_season_stats(self, obj):
        # Retrieve the season value from the context
        season = self.context.get('season', None)
        if season:
            # Fetch the season stats for the player for the specified season
            season_stats = obj.season_stats.filter(year=season).first()
            if season_stats:
                serializer = PlayerSeasonStatsSerializer(season_stats)
                return serializer.data
        return None

class PlayerSeasonStatsSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    player = serializers.SerializerMethodField()
    
    class Meta:
        model = PlayerSeasonStats
        fields = '__all__'

    def get_team(self, obj):
        serializer = FootballTeamSerializer(obj.team)
        return serializer.data
    
    def get_player(self, obj):
        serializer = FootballPlayerSerializer(obj.player)
        return serializer.data

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id','username','password','email', 'first_name', 'last_name']



class FootballPlayerAllSeasonsSerializer(serializers.ModelSerializer):
    team = FootballTeamSerializer(read_only=True)  # Always include team info
    seasons = serializers.SerializerMethodField()  # Renamed to reflect fetching all seasons

    class Meta:
        model = FootballPlayer
        fields = '__all__'  # Make sure 'team' and 'all_season_stats' are included

    def get_seasons(self, obj):
        # Fetch all season stats for the player
        season_stats = obj.season_stats.all().order_by('-year')
        serializer = PlayerSeasonStatsSerializer(season_stats, many=True)
        return serializer.data