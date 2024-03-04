from django.core.management.base import BaseCommand
from api.models import FootballTeam

# Define your NFL teams data
NFL_TEAMS = [
    #AFC East
    {
        "id": 1,  # Ensure unique IDs
        "team_name": "Buffalo Bills",
        "location": "Buffalo, New York",
        "abbreviation": "BUF",
        "team_color_primary": "#00338D",
        "team_color_secondary": "#C60C30",
        "coach": "Sean McDermott",
        "conference": "AFC",
        "division": "AFC East",
        "twitter_url": "https://twitter.com/buffalobills",
        "instagram_url": "https://www.instagram.com/buffalobills/",
        "facebook_url": "https://www.facebook.com/BuffaloBills",
        "last_season_wins": 0,  # Update with actual data
        "last_season_losses": 0,  # Update with actual data
        "last_season_ties": 0,  # Update with actual data
        "this_season_wins": 0,  # Update with actual data
        "this_season_losses": 0,  # Update with actual data
        "this_season_ties": 0,  # Update with actual data
        "stadium": "Highmark Stadium",
        "founded_year": 1960,
        "championships_won": 0,  # Update with actual data
        "logo_url": "",
        "official_website_url": "https://www.buffalobills.com/",
    },
    {
        "id": 2,
        "team_name": "Miami Dolphins",
        "location": "Miami Gardens, Florida",
        "abbreviation": "MIA",
        "team_color_primary": "#008E97",
        "team_color_secondary": "#FC4C02",
        "coach": "Mike McDaniel",
        "conference": "AFC",
        "division": "AFC East",
        "twitter_url": "https://twitter.com/MiamiDolphins",
        "instagram_url": "https://www.instagram.com/miamidolphins/",
        "facebook_url": "https://www.facebook.com/MiamiDolphins",
        "last_season_wins": 0,
        "last_season_losses": 0,
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Hard Rock Stadium",
        "founded_year": 1966,
        "championships_won": 0,  # Update with actual data
        "logo_url": "",
        "official_website_url": "https://www.miamidolphins.com/",
    },
    {
        "id": 3,
        "team_name": "New England Patriots",
        "location": "Foxborough, Massachusetts",
        "abbreviation": "NE",
        "team_color_primary": "#002244",
        "team_color_secondary": "#C60C30",
        "coach": "Bill Belichick",
        "conference": "AFC",
        "division": "AFC East",
        "twitter_url": "https://twitter.com/Patriots",
        "instagram_url": "https://www.instagram.com/patriots/",
        "facebook_url": "https://www.facebook.com/newenglandpatriots",
        "last_season_wins": 0,
        "last_season_losses": 0,
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Gillette Stadium",
        "founded_year": 1960,
        "championships_won": 0,  # Update with actual data
        "logo_url": "",
        "official_website_url": "https://www.patriots.com/",
    },
    {
        "id": 4,
        "team_name": "New York Jets",
        "location": "East Rutherford, New Jersey",
        "abbreviation": "NYJ",
        "team_color_primary": "#125740",
        "team_color_secondary": "#FFFFFF",
        "coach": "Robert Saleh",
        "conference": "AFC",
        "division": "AFC East",
        "twitter_url": "https://twitter.com/nyjets",
        "instagram_url": "https://www.instagram.com/nyjets/",
        "facebook_url": "https://www.facebook.com/Jets",
        "last_season_wins": 0,
        "last_season_losses": 0,
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "MetLife Stadium",
        "founded_year": 1960,
        "championships_won": 0,  # Update with actual data
        "logo_url": "",
        "official_website_url": "https://www.newyorkjets.com/",
    },
    # AFC South
        {
        "id": 5,
        "team_name": "Houston Texans",
        "location": "Houston, Texas",
        "abbreviation": "HOU",
        "team_color_primary": "#03202F",
        "team_color_secondary": "#A71930",
        "coach": "Lovie Smith",  # Please update this with the current coach if it has changed
        "conference": "AFC",
        "division": "AFC South",
        "twitter_url": "https://twitter.com/HoustonTexans",
        "instagram_url": "https://www.instagram.com/houstontexans/",
        "facebook_url": "https://www.facebook.com/HoustonTexans",
        "last_season_wins": 4,  # Placeholder, please update
        "last_season_losses": 13,  # Placeholder, please update
        "last_season_ties": 0,  # Typically, ties are rare
        "this_season_wins": 0,  # Placeholder, to be updated as the season progresses
        "this_season_losses": 0,  # Placeholder, to be updated as the season progresses
        "this_season_ties": 0,  # Placeholder, to be updated as the season progresses
        "stadium": "NRG Stadium",
        "founded_year": 2002,
        "championships_won": 0,  # Update if necessary
        "logo_url": "houston-texans-logo.png",
        "official_website_url": "https://www.houstontexans.com/",
    },
    {
        "id": 6,
        "team_name": "Indianapolis Colts",
        "location": "Indianapolis, Indiana",
        "abbreviation": "IND",
        "team_color_primary": "#002C5F",
        "team_color_secondary": "#A2AAAD",
        "coach": "Frank Reich",  # Please update this with the current coach if it has changed
        "conference": "AFC",
        "division": "AFC South",
        "twitter_url": "https://twitter.com/Colts",
        "instagram_url": "https://www.instagram.com/colts/",
        "facebook_url": "https://www.facebook.com/colts",
        "last_season_wins": 9,  # Placeholder, please update
        "last_season_losses": 8,  # Placeholder, please update
        "last_season_ties": 0,  # Typically, ties are rare
        "this_season_wins": 0,  # Placeholder, to be updated as the season progresses
        "this_season_losses": 0,  # Placeholder, to be updated as the season progresses
        "this_season_ties": 0,  # Placeholder, to be updated as the season progresses
        "stadium": "Lucas Oil Stadium",
        "founded_year": 1953,
        "championships_won": 2,  # Update if necessary
        "logo_url": "indianapolis-colts-logo.png",
        "official_website_url": "https://www.colts.com/",
    },
    {
        "id": 7,
        "team_name": "Jacksonville Jaguars",
        "location": "Jacksonville, Florida",
        "abbreviation": "JAX",
        "team_color_primary": "#006778",
        "team_color_secondary": "#9F792C",
        "coach": "Doug Pederson",  # Please update this with the current coach if it has changed
        "conference": "AFC",
        "division": "AFC South",
        "twitter_url": "https://twitter.com/Jaguars",
        "instagram_url": "https://www.instagram.com/jaguars/",
        "facebook_url": "https://www.facebook.com/jacksonvillejaguars",
        "last_season_wins": 3,  # Placeholder, please update
        "last_season_losses": 14,  # Placeholder, please update
        "last_season_ties": 0,  # Typically, ties are rare
        "this_season_wins": 0,  # Placeholder, to be updated as the season progresses
        "this_season_losses": 0,  # Placeholder, to be updated as the season progresses
        "this_season_ties": 0,  # Placeholder, to be updated as the season progresses
        "stadium": "TIAA Bank Field",
        "founded_year": 1995,
        "championships_won": 0,  # Update if necessary
        "logo_url": "jacksonville-jaguars-logo.png",
        "official_website_url": "https://www.jaguars.com/",
    },
    {
        "id": 8,
        "team_name": "Tennessee Titans",
        "location": "Nashville, Tennessee",
        "abbreviation": "TEN",
        "team_color_primary": "#0C2340",
        "team_color_secondary": "#4B92DB",
        "coach": "Mike Vrabel",  # Please update this with the current coach if it has changed
        "conference": "AFC",
        "division": "AFC South",
        "twitter_url": "https://twitter.com/Titans",
        "instagram_url": "https://www.instagram.com/titans/",
        "facebook_url": "https://www.facebook.com/titans",
        "last_season_wins": 12,  # Placeholder, please update
        "last_season_losses": 5,  # Placeholder, please update
        "last_season_ties": 0,  # Typically, ties are rare
        "this_season_wins": 0,  # Placeholder, to be updated as the season progresses
        "this_season_losses": 0,  # Placeholder, to be updated as the season progresses
        "this_season_ties": 0,  # Placeholder, to be updated as the season progresses
        "stadium": "Nissan Stadium",
        "founded_year": 1960,
        "championships_won": 0,  # Update if necessary
        "logo_url": "tennessee-titans-logo.png",
        "official_website_url": "https://www.tennesseetitans.com/",
    },
    # AFC North
        {
        "id": 9,
        "team_name": "Baltimore Ravens",
        "location": "Baltimore, Maryland",
        "abbreviation": "BAL",
        "team_color_primary": "#241773",
        "team_color_secondary": "#9E7C0C",
        "coach": "John Harbaugh",  # Verify for current season
        "conference": "AFC",
        "division": "AFC North",
        "twitter_url": "https://twitter.com/Ravens",
        "instagram_url": "https://www.instagram.com/ravens/",
        "facebook_url": "https://www.facebook.com/baltimoreravens",
        "last_season_wins": 8,  # Placeholder, update needed
        "last_season_losses": 9,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "M&T Bank Stadium",
        "founded_year": 1996,
        "championships_won": 2,  # Verify and update if necessary
        "logo_url": "baltimore-ravens-logo.png",
        "official_website_url": "https://www.baltimoreravens.com/",
    },
    {
        "id": 10,
        "team_name": "Cincinnati Bengals",
        "location": "Cincinnati, Ohio",
        "abbreviation": "CIN",
        "team_color_primary": "#FB4F14",
        "team_color_secondary": "#000000",
        "coach": "Zac Taylor",  # Verify for current season
        "conference": "AFC",
        "division": "AFC North",
        "twitter_url": "https://twitter.com/Bengals",
        "instagram_url": "https://www.instagram.com/bengals/",
        "facebook_url": "https://www.facebook.com/bengals",
        "last_season_wins": 10,  # Placeholder, update needed
        "last_season_losses": 7,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Paul Brown Stadium",
        "founded_year": 1968,
        "championships_won": 0,  # Verify and update if necessary
        "logo_url": "cincinnati-bengals-logo.png",
        "official_website_url": "https://www.bengals.com/",
    },
    {
        "id": 11,
        "team_name": "Cleveland Browns",
        "location": "Cleveland, Ohio",
        "abbreviation": "CLE",
        "team_color_primary": "#311D00",
        "team_color_secondary": "#FF3C00",
        "coach": "Kevin Stefanski",  # Verify for current season
        "conference": "AFC",
        "division": "AFC North",
        "twitter_url": "https://twitter.com/Browns",
        "instagram_url": "https://www.instagram.com/clevelandbrowns/",
        "facebook_url": "https://www.facebook.com/clevelandbrowns",
        "last_season_wins": 8,  # Placeholder, update needed
        "last_season_losses": 9,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "FirstEnergy Stadium",
        "founded_year": 1946,
        "championships_won": 0,  # Verify and update if necessary
        "logo_url": "cleveland-browns-logo.png",
        "official_website_url": "https://www.clevelandbrowns.com/",
    },
    {
        "id": 12,
        "team_name": "Pittsburgh Steelers",
        "location": "Pittsburgh, Pennsylvania",
        "abbreviation": "PIT",
        "team_color_primary": "#FFB612",
        "team_color_secondary": "#101820",
        "coach": "Mike Tomlin",  # Verify for current season
        "conference": "AFC",
        "division": "AFC North",
        "twitter_url": "https://twitter.com/steelers",
        "instagram_url": "https://www.instagram.com/steelers/",
        "facebook_url": "https://www.facebook.com/steelers",
        "last_season_wins": 9,  # Placeholder, update needed
        "last_season_losses": 7,  # Placeholder, update needed
        "last_season_ties": 1,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Heinz Field",
        "founded_year": 1933,
        "championships_won": 6,  # Verify and update if necessary
        "logo_url": "pittsburgh-steelers-logo.png",
        "official_website_url": "https://www.steelers.com/",
    },
    # AFC West
        {
        "id": 13,
        "team_name": "Denver Broncos",
        "location": "Denver, Colorado",
        "abbreviation": "DEN",
        "team_color_primary": "#FB4F14",
        "team_color_secondary": "#002244",
        "coach": "Nathaniel Hackett",  # Verify for the current season and update if necessary
        "conference": "AFC",
        "division": "AFC West",
        "twitter_url": "https://twitter.com/Broncos",
        "instagram_url": "https://www.instagram.com/broncos/",
        "facebook_url": "https://www.facebook.com/DenverBroncos",
        "last_season_wins": 7,  # Placeholder, update needed
        "last_season_losses": 10,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Empower Field at Mile High",
        "founded_year": 1960,
        "championships_won": 3,  # Verify and update if necessary
        "logo_url": "denver-broncos-logo.png",
        "official_website_url": "https://www.denverbroncos.com/",
    },
    {
        "id": 14,
        "team_name": "Kansas City Chiefs",
        "location": "Kansas City, Missouri",
        "abbreviation": "KC",
        "team_color_primary": "#E31837",
        "team_color_secondary": "#FFB81C",
        "coach": "Andy Reid",  # Verify for the current season and update if necessary
        "conference": "AFC",
        "division": "AFC West",
        "twitter_url": "https://twitter.com/Chiefs",
        "instagram_url": "https://www.instagram.com/chiefs/",
        "facebook_url": "https://www.facebook.com/KansasCityChiefs",
        "last_season_wins": 12,  # Placeholder, update needed
        "last_season_losses": 5,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Arrowhead Stadium",
        "founded_year": 1960,
        "championships_won": 2,  # Verify and update if necessary
        "logo_url": "kansas-city-chiefs-logo.png",
        "official_website_url": "https://www.chiefs.com/",
    },
    {
        "id": 15,
        "team_name": "Las Vegas Raiders",
        "location": "Las Vegas, Nevada",
        "abbreviation": "LV",
        "team_color_primary": "#000000",
        "team_color_secondary": "#A5ACAF",
        "coach": "Josh McDaniels",  # Verify for the current season and update if necessary
        "conference": "AFC",
        "division": "AFC West",
        "twitter_url": "https://twitter.com/Raiders",
        "instagram_url": "https://www.instagram.com/raiders/",
        "facebook_url": "https://www.facebook.com/Raiders",
        "last_season_wins": 6,  # Placeholder, update needed
        "last_season_losses": 11,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Allegiant Stadium",
        "founded_year": 1960,
        "championships_won": 3,  # Verify and update if necessary
        "logo_url": "las-vegas-raiders-logo.png",
        "official_website_url": "https://www.raiders.com/",
    },
    {
        "id": 16,
        "team_name": "Los Angeles Chargers",
        "location": "Los Angeles, California",
        "abbreviation": "LAC",
        "team_color_primary": "#0080C6",
        "team_color_secondary": "#FFC20E",
        "coach": "Brandon Staley",  # Verify for the current season and update if necessary
        "conference": "AFC",
        "division": "AFC West",
        "twitter_url": "https://twitter.com/chargers",
        "instagram_url": "https://www.instagram.com/chargers/",
        "facebook_url": "https://www.facebook.com/chargers",
        "last_season_wins": 9,  # Placeholder, update needed
        "last_season_losses": 8,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "SoFi Stadium",
        "founded_year": 1960,
        "championships_won": 0,  # Verify and update if necessary
        "logo_url": "los-angeles-chargers-logo.png",
        "official_website_url": "https://www.chargers.com/",
    },
    # NFC North
        {
        "id": 17,
        "team_name": "Chicago Bears",
        "location": "Chicago, Illinois",
        "abbreviation": "CHI",
        "team_color_primary": "#0B162A",
        "team_color_secondary": "#C83803",
        "coach": "Matt Eberflus",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC North",
        "twitter_url": "https://twitter.com/ChicagoBears",
        "instagram_url": "https://www.instagram.com/chicagobears/",
        "facebook_url": "https://www.facebook.com/ChicagoBears",
        "last_season_wins": 6,  # Placeholder, update needed
        "last_season_losses": 11,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Soldier Field",
        "founded_year": 1919,
        "championships_won": 9,  # Verify and update if necessary, including Super Bowls and pre-Super Bowl era championships
        "logo_url": "chicago-bears-logo.png",
        "official_website_url": "https://www.chicagobears.com/",
    },
    {
        "id": 18,
        "team_name": "Detroit Lions",
        "location": "Detroit, Michigan",
        "abbreviation": "DET",
        "team_color_primary": "#0076B6",
        "team_color_secondary": "#B0B7BC",
        "coach": "Dan Campbell",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC North",
        "twitter_url": "https://twitter.com/Lions",
        "instagram_url": "https://www.instagram.com/detroitlionsnfl/",
        "facebook_url": "https://www.facebook.com/DetroitLions",
        "last_season_wins": 3,  # Placeholder, update needed
        "last_season_losses": 13,  # Placeholder, update needed
        "last_season_ties": 1,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Ford Field",
        "founded_year": 1930,
        "championships_won": 4,  # Verify and update if necessary, including pre-Super Bowl era championships
        "logo_url": "detroit-lions-logo.png",
        "official_website_url": "https://www.detroitlions.com/",
    },
    {
        "id": 19,
        "team_name": "Green Bay Packers",
        "location": "Green Bay, Wisconsin",
        "abbreviation": "GB",
        "team_color_primary": "#203731",
        "team_color_secondary": "#FFB612",
        "coach": "Matt LaFleur",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC North",
        "twitter_url": "https://twitter.com/packers",
        "instagram_url": "https://www.instagram.com/packers/",
        "facebook_url": "https://www.facebook.com/Packers",
        "last_season_wins": 13,  # Placeholder, update needed
        "last_season_losses": 4,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Lambeau Field",
        "founded_year": 1919,
        "championships_won": 13,  # Verify and update if necessary, including both Super Bowls and NFL Championships before the Super Bowl era
        "logo_url": "green-bay-packers-logo.png",
        "official_website_url": "https://www.packers.com/",
    },
    {
        "id": 20,
        "team_name": "Minnesota Vikings",
        "location": "Minneapolis, Minnesota",
        "abbreviation": "MIN",
        "team_color_primary": "#4F2683",
        "team_color_secondary": "#FFC62F",
        "coach": "Kevin O'Connell",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC North",
        "twitter_url": "https://twitter.com/Vikings",
        "instagram_url": "https://www.instagram.com/vikings/",
        "facebook_url": "https://www.facebook.com/minnesotavikings",
        "last_season_wins": 7,  # Placeholder, update needed
        "last_season_losses": 9,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "U.S. Bank Stadium",
        "founded_year": 1960,
        "championships_won": 0,  # Verify and update if necessary, considering NFL Championships and Super Bowl appearances
        "logo_url": "minnesota-vikings-logo.png",
        "official_website_url": "https://www.vikings.com/",
    },
    # NFC East
        {
        "id": 21,
        "team_name": "Dallas Cowboys",
        "location": "Arlington, Texas",
        "abbreviation": "DAL",
        "team_color_primary": "#041E42",
        "team_color_secondary": "#869397",
        "coach": "Mike McCarthy",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC East",
        "twitter_url": "https://twitter.com/dallascowboys",
        "instagram_url": "https://www.instagram.com/dallascowboys/",
        "facebook_url": "https://www.facebook.com/DallasCowboys",
        "last_season_wins": 12,  # Placeholder, update needed
        "last_season_losses": 5,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "AT&T Stadium",
        "founded_year": 1960,
        "championships_won": 5,  # Verify and update if necessary
        "logo_url": "dallas-cowboys-logo.png",
        "official_website_url": "https://www.dallascowboys.com/",
    },
    {
        "id": 22,
        "team_name": "New York Giants",
        "location": "East Rutherford, New Jersey",
        "abbreviation": "NYG",
        "team_color_primary": "#0B2265",
        "team_color_secondary": "#A71930",
        "coach": "Brian Daboll",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC East",
        "twitter_url": "https://twitter.com/Giants",
        "instagram_url": "https://www.instagram.com/nygiants/",
        "facebook_url": "https://www.facebook.com/newyorkgiants",
        "last_season_wins": 4,  # Placeholder, update needed
        "last_season_losses": 13,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "MetLife Stadium",
        "founded_year": 1925,
        "championships_won": 4,  # Verify and update if necessary, including Super Bowl victories
        "logo_url": "new-york-giants-logo.png",
        "official_website_url": "https://www.giants.com/",
    },
    {
        "id": 23,
        "team_name": "Philadelphia Eagles",
        "location": "Philadelphia, Pennsylvania",
        "abbreviation": "PHI",
        "team_color_primary": "#004C54",
        "team_color_secondary": "#A5ACAF",
        "coach": "Nick Sirianni",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC East",
        "twitter_url": "https://twitter.com/Eagles",
        "instagram_url": "https://www.instagram.com/philadelphiaeagles/",
        "facebook_url": "https://www.facebook.com/philadelphiaeagles",
        "last_season_wins": 9,  # Placeholder, update needed
        "last_season_losses": 8,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Lincoln Financial Field",
        "founded_year": 1933,
        "championships_won": 1,  # Verify and update if necessary, including Super Bowl victories
        "logo_url": "philadelphia-eagles-logo.png",
        "official_website_url": "https://www.philadelphiaeagles.com/",
    },
    {
        "id": 24,
        "team_name": "Washington Commanders",
        "location": "Landover, Maryland",
        "abbreviation": "WAS",
        "team_color_primary": "#773141",
        "team_color_secondary": "#FFB612",
        "coach": "Ron Rivera",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC East",
        "twitter_url": "https://twitter.com/Commanders",
        "instagram_url": "https://www.instagram.com/commanders/",
        "facebook_url": "https://www.facebook.com/Commanders",
        "last_season_wins": 7,  # Placeholder, update needed
        "last_season_losses": 10,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "FedExField",
        "founded_year": 1932,
        "championships_won": 3,  # Verify and update if necessary, including Super Bowl victories
        "logo_url": "washington-commanders-logo.png",
        "official_website_url": "https://www.commanders.com/",
    },
    # NFC South
        {
        "id": 25,
        "team_name": "Atlanta Falcons",
        "location": "Atlanta, Georgia",
        "abbreviation": "ATL",
        "team_color_primary": "#A71930",
        "team_color_secondary": "#000000",
        "coach": "Arthur Smith",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC South",
        "twitter_url": "https://twitter.com/AtlantaFalcons",
        "instagram_url": "https://www.instagram.com/atlantafalcons/",
        "facebook_url": "https://www.facebook.com/atlantafalcons",
        "last_season_wins": 7,  # Placeholder, update needed
        "last_season_losses": 10,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Mercedes-Benz Stadium",
        "founded_year": 1966,
        "championships_won": 0,  # Verify and update if necessary, including Super Bowl appearances
        "logo_url": "atlanta-falcons-logo.png",
        "official_website_url": "https://www.atlantafalcons.com/",
    },
    {
        "id": 26,
        "team_name": "Carolina Panthers",
        "location": "Charlotte, North Carolina",
        "abbreviation": "CAR",
        "team_color_primary": "#0085CA",
        "team_color_secondary": "#101820",
        "coach": "Matt Rhule",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC South",
        "twitter_url": "https://twitter.com/Panthers",
        "instagram_url": "https://www.instagram.com/panthers/",
        "facebook_url": "https://www.facebook.com/CarolinaPanthers",
        "last_season_wins": 5,  # Placeholder, update needed
        "last_season_losses": 12,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Bank of America Stadium",
        "founded_year": 1995,
        "championships_won": 0,  # Verify and update if necessary, including NFC championships and Super Bowl appearances
        "logo_url": "carolina-panthers-logo.png",
        "official_website_url": "https://www.panthers.com/",
    },
    {
        "id": 27,
        "team_name": "New Orleans Saints",
        "location": "New Orleans, Louisiana",
        "abbreviation": "NO",
        "team_color_primary": "#D3BC8D",
        "team_color_secondary": "#101820",
        "coach": "Dennis Allen",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC South",
        "twitter_url": "https://twitter.com/Saints",
        "instagram_url": "https://www.instagram.com/saints/",
        "facebook_url": "https://www.facebook.com/neworleanssaints",
        "last_season_wins": 9,  # Placeholder, update needed
        "last_season_losses": 8,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Caesars Superdome",
        "founded_year": 1967,
        "championships_won": 1,  # Verify and update if necessary, including Super Bowl victories
        "logo_url": "new-orleans-saints-logo.png",
        "official_website_url": "https://www.neworleanssaints.com/",
    },
    {
        "id": 28,
        "team_name": "Tampa Bay Buccaneers",
        "location": "Tampa, Florida",
        "abbreviation": "TB",
        "team_color_primary": "#D50A0A",
        "team_color_secondary": "#34302B",
        "coach": "Todd Bowles",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC South",
        "twitter_url": "https://twitter.com/Buccaneers",
        "instagram_url": "https://www.instagram.com/buccaneers/",
        "facebook_url": "https://www.facebook.com/tampabaybuccaneers",
        "last_season_wins": 13,  # Placeholder, update needed
        "last_season_losses": 4,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Raymond James Stadium",
        "founded_year": 1976,
        "championships_won": 2,  # Verify and update if necessary, including Super Bowl victories
        "logo_url": "tampa-bay-buccaneers-logo.png",
        "official_website_url": "https://www.buccaneers.com/",
    },
    # NFC West
        {
        "id": 29,
        "team_name": "Arizona Cardinals",
        "location": "Glendale, Arizona",
        "abbreviation": "ARI",
        "team_color_primary": "#97233F",
        "team_color_secondary": "#000000",
        "coach": "Kliff Kingsbury",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC West",
        "twitter_url": "https://twitter.com/AZCardinals",
        "instagram_url": "https://www.instagram.com/azcardinals/",
        "facebook_url": "https://www.facebook.com/arizonacardinals",
        "last_season_wins": 11,  # Placeholder, update needed
        "last_season_losses": 6,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "State Farm Stadium",
        "founded_year": 1898,
        "championships_won": 2,  # Verify and update if necessary, including NFL championships before the Super Bowl era
        "logo_url": "arizona-cardinals-logo.png",
        "official_website_url": "https://www.azcardinals.com/",
    },
    {
        "id": 30,
        "team_name": "Los Angeles Rams",
        "location": "Inglewood, California",
        "abbreviation": "LAR",
        "team_color_primary": "#003594",
        "team_color_secondary": "#FFA300",
        "coach": "Sean McVay",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC West",
        "twitter_url": "https://twitter.com/RamsNFL",
        "instagram_url": "https://www.instagram.com/rams/",
        "facebook_url": "https://www.facebook.com/LosAngelesRams",
        "last_season_wins": 12,  # Placeholder, update needed
        "last_season_losses": 5,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "SoFi Stadium",
        "founded_year": 1936,
        "championships_won": 3,  # Verify and update if necessary, including Super Bowl victories
        "logo_url": "los-angeles-rams-logo.png",
        "official_website_url": "https://www.therams.com/",
    },
    {
        "id": 31,
        "team_name": "San Francisco 49ers",
        "location": "Santa Clara, California",
        "abbreviation": "SF",
        "team_color_primary": "#AA0000",
        "team_color_secondary": "#B3995D",
        "coach": "Kyle Shanahan",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC West",
        "twitter_url": "https://twitter.com/49ers",
        "instagram_url": "https://www.instagram.com/49ers/",
        "facebook_url": "https://www.facebook.com/SANFRANCISCO49ERS",
        "last_season_wins": 13,  # Placeholder, update needed
        "last_season_losses": 4,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Levi's Stadium",
        "founded_year": 1946,
        "championships_won": 5,  # Verify and update if necessary, including Super Bowl victories
        "logo_url": "san-francisco-49ers-logo.png",
        "official_website_url": "https://www.49ers.com/",
    },
    {
        "id": 32,
        "team_name": "Seattle Seahawks",
        "location": "Seattle, Washington",
        "abbreviation": "SEA",
        "team_color_primary": "#002244",
        "team_color_secondary": "#69BE28",
        "coach": "Pete Carroll",  # Verify for the current season and update if necessary
        "conference": "NFC",
        "division": "NFC West",
        "twitter_url": "https://twitter.com/Seahawks",
        "instagram_url": "https://www.instagram.com/seahawks/",
        "facebook_url": "https://www.facebook.com/Seahawks",
        "last_season_wins": 7,  # Placeholder, update needed
        "last_season_losses": 10,  # Placeholder, update needed
        "last_season_ties": 0,
        "this_season_wins": 0,
        "this_season_losses": 0,
        "this_season_ties": 0,
        "stadium": "Lumen Field",
        "founded_year": 1976,
        "championships_won": 1,  # Verify and update if necessary, including Super Bowl victories
        "logo_url": "seattle-seahawks-logo.png",
        "official_website_url": "https://www.seahawks.com/",
    }
]

class Command(BaseCommand):
    help = 'Seeds the database with NFL teams data'

    def handle(self, *args, **kwargs):
        for team_data in NFL_TEAMS:
            team_obj, created = FootballTeam.objects.update_or_create(
                id=team_data.get("id"),  # Assuming `id` is used to uniquely identify a team
                defaults=team_data,
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added team: {team_data["team_name"]}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated team: {team_data["team_name"]}'))

