def GetDefaultScoringParams():
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