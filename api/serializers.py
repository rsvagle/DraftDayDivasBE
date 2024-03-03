from rest_framework import serializers
from django.contrib.auth.models import User

from .models import DraftedTeam, FootballPlayer
from .models import NewsArticle

class DraftedTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftedTeam
        fields = ['id', 'userID', 'teamName', 'created_at']

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'author', 'title', 'description', 'article_content', 'image_url', 'created_at']



class FootballPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballPlayer
        fields = '__all__'

class FootballPlayerSummarySerializer(serializers.Serializer):
    # All FootballPlayer fields are included
    first_name = serializers.CharField(max_length=60)
    last_name = serializers.CharField(max_length=60)
    position = serializers.CharField(max_length=30)
    team_name = serializers.CharField(read_only=True)
    number = serializers.IntegerField(allow_null=True, required=False)
    height = serializers.CharField(max_length=10)
    weight = serializers.IntegerField(allow_null=True, required=False)
    date_of_birth = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d', 'iso-8601'], allow_null=True, required=False)
    years_pro = serializers.IntegerField()
    college = serializers.CharField(max_length=100, allow_blank=True, required=False)
    photo_url = serializers.URLField(max_length=200, allow_blank=True, required=False)

    # Additional fields
    season_passing_yards = serializers.IntegerField()
    season_passing_tds = serializers.IntegerField()
    season_rushing_yards = serializers.IntegerField()
    season_rushing_tds = serializers.IntegerField()
    season_receiving_yards = serializers.IntegerField()
    season_receiving_tds = serializers.IntegerField()
    season_fantasy_points = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id','username','password','email', 'first_name', 'last_name']