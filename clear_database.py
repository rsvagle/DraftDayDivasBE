from api.models import FootballPlayer, PlayerGameLog, PlayerSeasonStats, InjuryReportArticle
from generate_injury_reports import generate_injury_report_articles
from generate_players_seasons import generate_player_seasons
from generate_players import generate_players
from generate_player_game_logs import generate_player_game_logs

def clear_db():
    InjuryReportArticle.objects.all().delete()
    print("Injury reports clear")
    PlayerSeasonStats.objects.all().delete()
    print("Player Seasons Clear")
    PlayerGameLog.objects.all().delete()
    print("Player Game Logs Clear")
    FootballPlayer.objects.all().delete()
    print("Players clear")

def generate_db():
    generate_players()
    generate_player_game_logs()
    generate_injury_report_articles(35)