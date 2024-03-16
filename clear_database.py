from api.models import FootballPlayer, PlayerSeasonStats, InjuryReportArticle
from generate_injury_reports import generate_injury_report_articles
from generate_players_seasons import generate_player_seasons
from generate_players import generate_players

def clear_db():
    InjuryReportArticle.objects.all().delete()
    print("Injury reports clear")
    PlayerSeasonStats.objects.all().delete()
    print("Player Seasons Clear")
    FootballPlayer.objects.all().delete()
    print("Players clear")

def generate_db():
    generate_players()
    generate_player_seasons()
    generate_injury_report_articles(35)