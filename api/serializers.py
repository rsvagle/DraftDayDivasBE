from rest_framework import serializers
from django.contrib.auth.models import User

from .models import DraftedTeam, FootballPlayer, FootballTeam, InjuryReportArticle, PlayerSeasonStats
from .models import NewsArticle

# Drafted Team
class DraftedTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftedTeam
        fields = ['id', 'userID', 'teamName', 'created_at']

# News Article
class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'author', 'title', 'description', 'article_content', 'image_url', 'created_at']

# Injury Report
class InjuryReportArticleSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField()

    class Meta:
        model = InjuryReportArticle
        fields = ['id', 'author', 'player', 'title', 'description', 'article_content', 'image_url', 'created_at']

    def get_player(self, obj):
        if obj.player:
            serializer = FootballPlayerSerializer(obj.player)
            return serializer.data
        else:
            return None

# Football team - return all
class FootballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballTeam
        fields = '__all__'

# Football Player - Pass in season
class FootballPlayerSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    stats_for_season = serializers.SerializerMethodField()  # Renamed to reflect dynamic season functionality

    class Meta:
        model = FootballPlayer
        fields = '__all__'
    
    def get_team(self, obj):
        if self.context.get('include_team', False):
            serializer = FootballTeamSerializer(obj.team)
            return serializer.data
        else:
            return obj.team_id

    def get_stats_for_season(self, obj):
        # Retrieve the season value from the context
        season = self.context.get('season', None)
        if season:
            # Fetch the season stats for the player for the specified season
            season_stats = obj.season_stats.filter(year=season).order_by('year').first()
            if season_stats:
                serializer = PlayerSeasonStatsSerializer(season_stats)
                return serializer.data
        return None

from .utils import GetDefaultScoringParams

# Player summary
# Pulls team and latest season
class FootballPlayerSummarySerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    season_stats = serializers.SerializerMethodField()

    projected_points = serializers.FloatField(read_only=True)
    ranking = serializers.IntegerField(read_only=True)

    class Meta:
        model = FootballPlayer
        fields = '__all__'
    
    def get_team(self, obj):
        if self.context.get('include_team', True):
            from .serializers import FootballTeamSerializer  # Import here to avoid circular dependency
            serializer = FootballTeamSerializer(obj.team)
            return serializer.data
        else:
            return obj.team_id

    def get_season_stats(self, obj):
        # Fetch the season stats for the player for the specified season
        season_stats = obj.season_stats.order_by("-year").first()
        if season_stats:
            from .serializers import PlayerSeasonStatsSerializer  # Import here to avoid circular dependency
            serializer = PlayerSeasonStatsSerializer(season_stats)
            data = serializer.data
            
            # Calculate fantasy points
            scoring_params = self.context.get('scoring_params', GetDefaultScoringParams())
            fantasy_points = self.calculate_fantasy_points(season_stats, scoring_params)
            data['fantasy_points'] = fantasy_points  # Add fantasy points to the serialized data
            
            return data
        return None

    def calculate_fantasy_points(self, season_stats, scoring_params):
        fantasy_points = 0
        fantasy_points += season_stats.passing_yards * scoring_params.get('passing_yards', 0)
        fantasy_points += season_stats.passing_tds * scoring_params.get('passing_tds', 0)

        fantasy_points += season_stats.rushing_yards * scoring_params.get('rushing_yards', 0)
        fantasy_points += season_stats.rushing_tds * scoring_params.get('rushing_tds', 0)

        fantasy_points += season_stats.receptions * scoring_params.get('receptions', 0)
        fantasy_points += season_stats.receiving_yards * scoring_params.get('receiving_yards', 0)
        fantasy_points += season_stats.receiving_tds * scoring_params.get('receiving_tds', 0)

        fantasy_points += season_stats.fgm0_19 * scoring_params.get('fgm0_19', 0)
        fantasy_points += season_stats.fgm20_39 * scoring_params.get('fgm20_39', 0)
        fantasy_points += season_stats.fgm40_49 * scoring_params.get('fgm40_49', 0)
        fantasy_points += season_stats.fgm50_plus * scoring_params.get('fgm50_plus', 0)
        fantasy_points += season_stats.xpm * scoring_params.get('xpm', 0)
        
        # Add other scoring calculations as needed
        return round(fantasy_points, 2)

# Season statline for a player
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

# Website user
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id','username','password','email', 'first_name', 'last_name']


# Player with all season data
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