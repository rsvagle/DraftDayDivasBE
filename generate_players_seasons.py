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

            season_fgm0_19 = 0
            season_fgm20_39 = 0
            season_fgm40_49 = 0
            season_fgm50_plus = 0

            season_fga = 0
            season_xpm = 0
            season_xpa = 0

            match player.position:
                case "QB":
                    season_passing_yards = random.randint(2500, 5000)
                    season_passing_tds = random.randint(16, 45)
                    season_passing_rating = 1
                    season_ints = random.randint(3,15)
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
                    season_fgm0_19 = random.randint(2, 8)
                    season_fgm20_39 = random.randint(5, 15)
                    season_fgm40_49 = random.randint(5, 15)
                    season_fgm50_plus = random.randint(0,8)

                    total_fg = season_fgm0_19 + season_fgm20_39 + season_fgm40_49 + season_fgm50_plus
                    random_fg_percentage = random.randint(70,100) / 100.0
                    random_fg_inverse = 1 / random_fg_percentage

                    season_fga = math.floor(total_fg*random_fg_inverse)
                    season_xpa = random.randint(30, 55)
                    season_xpm = random.randint(math.floor(season_xpa * .8), season_xpa)
                case _:
                    pass


            player_season_stats = PlayerSeasonStats (
                id=id,
                player=season_player,
                team=season_team,
                year=season_year,
                games_played = season_games_played,
                passing_yards = season_passing_yards,
                passing_tds = season_passing_tds,
                passer_rating = season_passing_rating,
                ints = season_ints,
                fumbles = season_fumbles,
                fumbles_lost = season_fumbles_lost,
                safeties = season_safeties,
                rushing_yards = season_rushing_yards,
                rushing_tds = season_rushing_tds,
                receptions = season_receptions,
                receiving_yards = season_receiving_yards,
                receiving_tds = season_receiving_tds,
                fgm0_19 = season_fgm0_19,
                fgm20_39 =  season_fgm20_39,
                fgm40_49 =  season_fgm40_49,
                fgm50_plus = season_fgm50_plus,
                fga = season_fga,
                xpm = season_xpm,
                xpa = season_xpa,
            )

            all_seasons.append(player_season_stats)
    
    PlayerSeasonStats.objects.bulk_create(all_seasons)

if __name__ == "__main__":
    generate_player_seasons()

def show_players():
    players = FootballPlayer.objects.all()

    for player in players:
        print(player.name, player.years_pro)