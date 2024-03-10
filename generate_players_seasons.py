import random
import math
from faker import Faker
from datetime import datetime
from api.models import FootballPlayer, PlayerSeasonStats

faker = Faker()

def generate_player_seasons():
    all_seasons = []

    # Get a player
    players = FootballPlayer.objects.all()

    for player in players:
        print(player.first_name, player.years_pro)
        # For every year pro, make a season
        for year in range(0, player.years_pro):
            # Make a season
            id = faker.unique.random_int(min=1, max=10000)
            season_player = player
            season_team = player.team
            season_year = 2024-year
            season_games_played = 16

            season_passing_yards = 0
            season_passing_tds = 0
            season_passing_rating = 0

            season_ints = 0
            season_fumbles = 0
            season_fumbles_lost = 0
            season_safeties = 0

            season_rushing_yards = 0
            season_rushing_tds = 0

            season_receptions = 0
            season_receiving_yards = 0
            season_receiving_tds = 0

            season_fgm = 0
            season_fga = 0
            season_xpm = 0
            season_xpa = 0

            season_fantasy_points = 0

            match player.position:
                case "QB":
                    season_passing_yards = random.randint(2500, 5000)
                    season_passing_tds = random.randint(16, 45)
                    season_passing_rating = 1
                    season_ints = random.randint(4, 16)
                    season_fumbles = random.randint(0, 5)
                    season_fumbles_lost = random.randint(0, season_fumbles_lost)
                    season_rushing_yards = random.randint(0, 300)
                    season_rushing_tds = random.randint(0, 5)
                case "RB":
                    season_rushing_yards = random.randint(500, 1800)
                    season_rushing_tds = random.randint(0, 17)
                    season_fumbles = random.randint(0, 3)
                    season_fumbles_lost = random.randint(0, season_fumbles)
                    season_receptions = random.randint(0, 50)
                    season_receiving_yards = random.randint(0, 400)
                    season_receiving_tds = random.randint(0, 5)
                case "WR":                
                    season_receptions = random.randint(35, 110)
                    season_receiving_yards = season_receptions * random.randint(8, 15)
                    season_receiving_tds = random.randint(0, 15)
                    season_fumbles = random.randint(0, 2)
                    season_fumbles_lost = random.randint(0, season_fumbles)
                case "TE":
                    season_receptions = random.randint(35, 110)
                    season_receiving_yards = season_receptions * random.randint(8, 15)
                    season_receiving_tds = random.randint(0, 15)
                    season_fumbles = random.randint(0, 2)
                    season_fumbles_lost = random.randint(0, season_fumbles)
                case "K":
                    season_fga = random.randint(22, 35)
                    season_fgm = random.randint(season_fga // 2, season_fga)
                    season_xpa = random.randint(30, 55)
                    season_xpm = random.randint(math.floor(season_xpm * .8), season_xpm)
                case _:
                    pass


            player_season_stats = PlayerSeasonStats (
                id=id,
                player=season_player,
                team=season_team,
                season=season_year,
                games_played = season_games_played,
                season_passing_yards = season_passing_yards,
                season_passing_tds = season_passing_tds,
                season_passer_rating = season_passing_rating,
                season_ints = season_ints,
                season_fumbles = season_fumbles,
                season_fumbles_lost = season_fumbles_lost,
                season_safeties = season_safeties,
                season_rushing_yards = season_rushing_yards,
                season_rushing_tds = season_rushing_tds,
                season_receptions = season_receptions,
                season_receiving_yards = season_receiving_yards,
                season_receiving_tds = season_receiving_tds,
                season_fgm = season_fgm,
                season_fga = season_fga,
                season_xpm = season_xpm,
                season_xpa = season_xpa,
                season_fantasy_points = season_fantasy_points
            )

            player_season_stats = calculate_fantasy_points(player_season_stats)

            all_seasons.append(player_season_stats)
    
    PlayerSeasonStats.objects.bulk_create(all_seasons)


def calculate_fantasy_points(player_season_stats):
    player_season_stats.season_fantasy_points = 0

    player_season_stats.season_fantasy_points += player_season_stats.season_passing_yards * .04
    player_season_stats.season_fantasy_points += player_season_stats.season_passing_tds * 4
    player_season_stats.season_fantasy_points += player_season_stats.season_ints * -2
    player_season_stats.season_fantasy_points += player_season_stats.season_fumbles_lost * -2
    player_season_stats.season_fantasy_points += player_season_stats.season_rushing_yards * .1
    player_season_stats.season_fantasy_points += player_season_stats.season_rushing_tds * 6
    player_season_stats.season_fantasy_points += player_season_stats.season_receptions * .5
    player_season_stats.season_fantasy_points += player_season_stats.season_receiving_yards * .1
    player_season_stats.season_fantasy_points += player_season_stats.season_receiving_tds * 6
    player_season_stats.season_fantasy_points += player_season_stats.season_fgm * 3
    player_season_stats.season_fantasy_points += player_season_stats.season_xpm * 1

    return player_season_stats

if __name__ == "__main__":
    generate_player_seasons()

def show_players():
    players = FootballPlayer.objects.all()

    for player in players:
        print(player.name, player.years_pro)