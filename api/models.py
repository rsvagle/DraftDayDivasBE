from django.db import models
import string
import random
from random import randint

# Create your models here.
CONFERENCE_CHOICES = (
    ('AFC', 'American Football Conference'),
    ('NFC', 'National Football Conference'),
)

DIVISION_CHOICES = (
    ('AFC North', 'AFC North'),
    ('AFC South', 'AFC South'),
    ('AFC East', 'AFC East'),
    ('AFC West', 'AFC West'),
    ('NFC North', 'NFC North'),
    ('NFC South', 'NFC South'),
    ('NFC East', 'NFC East'),
    ('NFC West', 'NFC West'),
)

def generate_unique_teamname():
    length = 14

    while True:
        teamName = ''.join(random.choices(string.ascii_lowercase, k=length))
        if DraftedTeam.objects.filter(teamName=teamName).count() == 0:
            break
        
        return teamName

class DraftedTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    team_name = models.CharField(max_length=60, default="")
    created_at = models.DateTimeField(auto_now_add=True)

class NewsArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=60, default="")
    date = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=500, default="")
    description =models.CharField(max_length=500, default="")
    article_content = models.CharField(max_length=5000, default="")
    image_url = models.CharField(max_length=5000, default="")
    created_at = models.DateTimeField(auto_now_add=True)

class FootballTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=60, default="")
    location = models.CharField(max_length=100, default="")
    abbreviation = models.CharField(max_length=3, default="")
    team_color_primary = models.CharField(max_length=7, default="")
    team_color_secondary = models.CharField(max_length=7, default="")
    coach = models.CharField(max_length=100, default="")
    conference = models.CharField(max_length=3, choices=CONFERENCE_CHOICES, default="")
    division = models.CharField(max_length=50, choices=DIVISION_CHOICES, default="")
    twitter_url = models.CharField(max_length=200, default="", blank=True)
    instagram_url = models.CharField(max_length=200, default="", blank=True)
    facebook_url = models.CharField(max_length=200, default="", blank=True)
    last_season_wins = models.IntegerField(default=0)
    last_season_losses = models.IntegerField(default=0)
    last_season_ties = models.IntegerField(default=0)
    this_season_wins = models.IntegerField(default=0)
    this_season_losses = models.IntegerField(default=0)
    this_season_ties = models.IntegerField(default=0)
    stadium = models.CharField(max_length=100, default="")
    founded_year = models.IntegerField(null=True, blank=True)
    championships_won = models.IntegerField(default=0)
    logo_url = models.CharField(max_length=200, default="")
    official_website_url = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(auto_now_add=True)

class FootballPlayer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=60, default="")
    last_name = models.CharField(max_length=60, default="")
    position = models.CharField(max_length=30, default="")
    team = models.ForeignKey(FootballTeam, on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)
    height = models.CharField(max_length=10, default="")
    weight = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    years_pro = models.IntegerField(default=0)
    college = models.CharField(max_length=100, default="", blank=True)
    photo_url = models.CharField(max_length=200, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PlayerSeasonStats(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE, related_name='season_stats')
    year = models.CharField(max_length=10)  # Example: "2023"
    team = models.ForeignKey(FootballTeam, on_delete=models.CASCADE, related_name='season_team')
    games_played = models.IntegerField()
    
    passing_yards = models.IntegerField()
    passing_tds = models.IntegerField()
    passer_rating = models.FloatField()

    ints = models.IntegerField()
    fumbles = models.IntegerField()
    fumbles_lost = models.IntegerField()
    safeties = models.IntegerField()

    rushing_yards = models.IntegerField()
    rushing_tds = models.IntegerField()

    receptions = models.IntegerField()
    receiving_yards = models.IntegerField()
    receiving_tds = models.IntegerField()

    fgm0_19 = models.IntegerField()
    fgm20_39 = models.IntegerField()
    fgm40_49 = models.IntegerField()
    fgm50_plus = models.IntegerField()
    fga = models.IntegerField()

    xpm = models.IntegerField()
    xpa = models.IntegerField()

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} - {self.year}"

class InjuryReportArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=60, default="")
    date = models.DateTimeField(null=True, blank=True)
    player = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, default="")
    description = models.CharField(max_length=500, default="")
    article_content = models.CharField(max_length=5000, default="")
    image_url = models.CharField(max_length=5000, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

# This class is used purely for structuring data, not for creating a new table
class FootballPlayerSummary:
    def __init__(self, football_player):
        self.__dict__ = football_player.__dict__.copy()
        self.team_name = football_player.team.team_name
        self.season_passing_yards = randint(0, 500)
        self.season_passing_tds = randint(0, 50)
        self.season_rushing_yards = randint(0, 500)
        self.season_rushing_tds = randint(0, 20)
        self.season_receiving_yards = randint(0, 500)
        self.season_receiving_tds = randint(0, 20)
        self.season_fantasy_points = randint(0, 500)


class PlayerGameLog(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE, related_name='game_log')
    year = models.CharField(max_length=10)
    team = models.ForeignKey(FootballTeam, on_delete=models.CASCADE, related_name='game_team')
    week = models.IntegerField()
    opponent = models.ForeignKey(FootballTeam, on_delete=models.CASCADE, related_name='game_opponent')
    home = models.BooleanField()

    passing_yards = models.IntegerField()
    passing_tds = models.IntegerField()
    passer_rating = models.FloatField()

    ints = models.IntegerField()
    fumbles = models.IntegerField()
    fumbles_lost = models.IntegerField()
    safeties = models.IntegerField()

    rushing_yards = models.IntegerField()
    rushing_tds = models.IntegerField()

    receptions = models.IntegerField()
    receiving_yards = models.IntegerField()
    receiving_tds = models.IntegerField()

    fgm0_19 = models.IntegerField()
    fgm20_39 = models.IntegerField()
    fgm40_49 = models.IntegerField()
    fgm50_plus = models.IntegerField()
    fga = models.IntegerField()

    xpm = models.IntegerField()
    xpa = models.IntegerField()

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} - {self.year} Wk {self.week}"
    



class WeeklyPrediction(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE, related_name='weekly_pred')

    passing_yards = models.IntegerField()
    passing_tds = models.IntegerField()
    passer_rating = models.FloatField()

    ints = models.IntegerField()
    fumbles_lost = models.IntegerField()

    rushing_yards = models.IntegerField()
    rushing_tds = models.IntegerField()

    receptions = models.IntegerField()
    receiving_yards = models.IntegerField()
    receiving_tds = models.IntegerField()

    fgm0_19 = models.IntegerField()
    fgm20_39 = models.IntegerField()
    fgm40_49 = models.IntegerField()
    fgm50_plus = models.IntegerField()
    fga = models.IntegerField()

    xpm = models.IntegerField()
    xpa = models.IntegerField()

    standard_points= models.FloatField()
    ppr_points= models.FloatField()
    half_ppr_points= models.FloatField()

    prediction_comment = models.CharField()