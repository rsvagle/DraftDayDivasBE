# No PPR scoring params
def GetNoPPRScoringParams():
    scoring = {
        "passing_yards": .04,
        "passing_tds": 4,

        "rushing_yards": .1,
        "rushing_tds": 6,

        "receptions" : 0,
        "receiving_yards": .1,
        "receiving_tds": 6,
        
        "fgm0_19": 3,
        "fgm20_39": 3,
        "fgm40_49": 4,
        "fgm50_plus": 5,
        "xpm": 1
    }
    return scoring

# Half point PPR scoring params
def GetHalfPPRScoringParams():
    scoring = {
        "passing_yards": .04,
        "passing_tds": 4,

        "rushing_yards": .1,
        "rushing_tds": 6,

        "receptions" : 0.5,
        "receiving_yards": .1,
        "receiving_tds": 6,
        
        "fgm0_19": 3,
        "fgm20_39": 3,
        "fgm40_49": 4,
        "fgm50_plus": 5,
        "xpm": 1
    }
    return scoring

# PPR scoring params
def GetPPRScoringParams():
    scoring = {
        "passing_yards": .04,
        "passing_tds": 4,

        "rushing_yards": .1,
        "rushing_tds": 6,

        "receptions" : 1,
        "receiving_yards": .1,
        "receiving_tds": 6,
        
        "fgm0_19": 3,
        "fgm20_39": 3,
        "fgm40_49": 4,
        "fgm50_plus": 5,
        "xpm": 1
    }
    return scoring

# Calculate fantasy points for the stat totals based on the scoring params given
def calc_game_f_points(game_log, scoring_params):
    fantasy_points = 0
    fantasy_points += game_log.passing_yards * scoring_params.get('passing_yards', 0)
    fantasy_points += game_log.passing_tds * scoring_params.get('passing_tds', 0)

    fantasy_points += game_log.rushing_yards * scoring_params.get('rushing_yards', 0)
    fantasy_points += game_log.rushing_tds * scoring_params.get('rushing_tds', 0)

    fantasy_points += game_log.receptions * scoring_params.get('receptions', 0)
    fantasy_points += game_log.receiving_yards * scoring_params.get('receiving_yards', 0)
    fantasy_points += game_log.receiving_tds * scoring_params.get('receiving_tds', 0)

    fantasy_points += game_log.fgm0_19 * scoring_params.get('fgm0_19', 0)
    fantasy_points += game_log.fgm20_39 * scoring_params.get('fgm20_39', 0)
    fantasy_points += game_log.fgm40_49 * scoring_params.get('fgm40_49', 0)
    fantasy_points += game_log.fgm50_plus * scoring_params.get('fgm50_plus', 0)
    fantasy_points += game_log.xpm * scoring_params.get('xpm', 0)

    return round(fantasy_points,2)