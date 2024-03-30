import random
import math
import numpy as np
from faker import Faker
from datetime import datetime
from api.models import FootballPlayer, FootballTeam, PlayerGameLog, PlayerSeasonStats

faker = Faker()
faker2 = Faker()

def generate_player_game_logs():
    all_seasons = []

    # Get a player
    players = FootballPlayer.objects.all()

    season_id_index = 1
    game_id_index = 1

    for player in players:
        print(player.first_name, player.last_name, player.years_pro)
        bias = 0.6 # Add a boost for starters

        if(player.id <= 160):
            bias = max(1,np.random.normal(1.25, 0.25, 1))

        if player.years_pro == 0:
            season_id = season_id_index

            # Put into season stats object
            player_season_stats = PlayerSeasonStats (
                id=season_id,
                player=player,
                team=player.team,
                year=2024,
                games_played = 0,
                passing_yards = 0,
                passing_tds = 0,
                passer_rating = 0,
                ints = 0,
                fumbles = 0,
                fumbles_lost = 0,
                safeties = 0,
                rushing_yards = 0,
                rushing_tds = 0,
                receptions = 0,
                receiving_yards = 0,
                receiving_tds = 0,
                fgm0_19 = 0,
                fgm20_39 =  0,
                fgm40_49 =  0,
                fgm50_plus = 0,
                fga = 0,
                xpm = 0,
                xpa = 0,
            )

            all_seasons.append(player_season_stats)
            season_id_index += 1

        else:              
            # For every year pro, make a season
            for year in range(0, player.years_pro):
                year_game_logs = []

                # Track season stats
                season_id = season_id_index
                season_player = player
                season_team = player.team
                season_year = 2024-year

                season_games_played = 0
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

                for week in range(1, 18):
                    # Make a game log
                    id = game_id_index
                    player = player
                    team = player.team
                    week = week
                    home = random.randint(0,1)

                    opponent_id = random.randint(1, 32)

                    while(opponent_id == player.team.id):
                        opponent_id = random.randint(1, 32)

                    opponent = FootballTeam.objects.get(id=opponent_id)
                    
                    passing_yards = 0
                    passing_tds = 0
                    passing_rating = 0

                    ints = 0
                    fumbles = 0
                    fumbles_lost = 0
                    safeties = 0

                    rushing_yards = 0
                    rushing_tds = 0

                    receptions = 0
                    receiving_yards = 0
                    receiving_tds = 0

                    fgm0_19 = 0
                    fgm20_39 = 0
                    fgm40_49 = 0
                    fgm50_plus = 0

                    fga = 0
                    xpm = 0
                    xpa = 0

                    # Create game stats
                    match player.position:
                        case "QB":
                            passing_yards = math.floor(np.random.normal(min(300,200*bias), 25*bias, 1))
                            passing_tds = math.floor(np.random.normal(1.75*bias, 0.5, 1))
                            passing_rating = 1
                            ints = max(math.floor(np.random.normal(0.5, 0.5, 1)),0)
                            fumbles = max(math.floor(np.random.normal(0.25, 0.5, 1)),0)
                            fumbles_lost = random.randint(0, fumbles)
                            rushing_yards = max(math.floor(np.random.normal(12, 12, 1)),0)
                            rushing_tds = max(math.floor(np.random.normal(0.25, 0.5, 1)),0)
                        case "RB":
                            rushing_yards = max(math.floor(np.random.normal(58*bias, 35, 1)),0)
                            rushing_tds = max(math.floor(np.random.normal(0.6, 0.8, 1)),0)
                            fumbles = max(math.floor(np.random.normal(0.2, 0.5, 1)),0)
                            fumbles_lost = random.randint(0, fumbles)
                            receptions = random.randint(0, 5)
                            receiving_yards = max(math.floor(np.random.normal(15, 15, 1)),0)
                            receiving_tds = max(math.floor(np.random.normal(0.3, 0.5, 1)),0)
                        case "WR":                
                            receptions = max(math.floor(np.random.normal(3.5*bias, 2, 1)),0)
                            receiving_yards = receptions * max(math.floor(np.random.normal(8*bias, 5, 1)),4)
                            receiving_tds = max(math.floor(np.random.normal(0.6, 0.8, 1)),0)
                            fumbles = max(math.floor(np.random.normal(0.1, 0.25, 1)),0)
                            fumbles_lost = random.randint(0, fumbles)
                        case "TE":
                            receptions = max(math.floor(np.random.normal(2.7*bias, 1.5, 1)),0)
                            receiving_yards = receptions * max(math.floor(np.random.normal(7*bias, 4, 1)),4)
                            receiving_tds = max(math.floor(np.random.normal(0.6, 0.7, 1)),0)
                            fumbles = max(math.floor(np.random.normal(0.05, 0.25, 1)),0)
                            fumbles_lost = random.randint(0, fumbles)
                        case "K":
                            fgm0_19 = max(math.floor(np.random.normal(0.5, 0.5, 1)),0)
                            fgm20_39 = max(math.floor(np.random.normal(0.5, 0.5, 1)),0)
                            fgm40_49 = max(math.floor(np.random.normal(0.5, 0.5, 1)),0)
                            fgm50_plus = max(math.floor(np.random.normal(0.5, 0.5, 1)),0)

                            total_fg = fgm0_19 + fgm20_39 + fgm40_49 + fgm50_plus
                            random_fg_percentage = random.randint(70,100) / 100.0
                            random_fg_inverse = 1 / random_fg_percentage

                            fgmissed = max(math.floor(np.random.normal(0.5, 0.25, 1)),0)
                            fga = total_fg+fgmissed

                            xpm = max(0,math.floor(np.random.normal(2.5, 0.5, 1)))
                            xpmissed = max(math.floor(np.random.normal(0.2, 0.25, 1)),0)
                            xpa = xpm + xpmissed
                        case _:
                            pass

                    game_log = PlayerGameLog (
                        id=id,
                        player=player,
                        team=team,
                        year=season_year,
                        week=week,
                        home = home,
                        opponent = opponent,
                        passing_yards = passing_yards,
                        passing_tds = passing_tds,
                        passer_rating = passing_rating,
                        ints = ints,
                        fumbles = fumbles,
                        fumbles_lost = fumbles_lost,
                        safeties = safeties,
                        rushing_yards = rushing_yards,
                        rushing_tds = rushing_tds,
                        receptions = receptions,
                        receiving_yards = receiving_yards,
                        receiving_tds = receiving_tds,
                        fgm0_19 = fgm0_19,
                        fgm20_39 =  fgm20_39,
                        fgm40_49 =  fgm40_49,
                        fgm50_plus = fgm50_plus,
                        fga = fga,
                        xpm = xpm,
                        xpa = xpa,
                    )

                    year_game_logs.append(game_log)

                    game_id_index += 1

                    # Add to season stats
                    season_games_played += 1

                    season_passing_yards += passing_yards
                    season_passing_tds += passing_tds

                    season_ints += ints
                    season_fumbles += fumbles
                    season_fumbles_lost += fumbles_lost
                    season_safeties += safeties

                    season_rushing_yards += rushing_yards
                    season_rushing_tds += rushing_tds

                    season_receptions += receptions
                    season_receiving_yards += receiving_yards
                    season_receiving_tds += receiving_tds

                    season_fgm0_19 += fgm0_19
                    season_fgm20_39 += fgm20_39
                    season_fgm40_49 += fgm40_49
                    season_fgm50_plus += fgm50_plus

                    season_fga += fga
                    season_xpm += xpm
                    season_xpa += xpa

                # Put into season stats object
                player_season_stats = PlayerSeasonStats (
                    id=season_id,
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
                season_id_index += 1

                PlayerGameLog.objects.bulk_create(year_game_logs)    
    
    PlayerSeasonStats.objects.bulk_create(all_seasons)

if __name__ == "__main__":
    generate_player_game_logs()

def show_players():
    players = FootballPlayer.objects.all()

    for player in players:
        print(player.name, player.years_pro)