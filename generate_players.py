import random
from faker import Faker
from datetime import datetime
from api.models import FootballPlayer, FootballTeam, NewsArticle

faker = Faker()

def generate_players():
    positions = ["QB", "RB", "WR", "TE", "K"]

    for id in range(2, 102):  # IDs from 2 to 101
        first_name = faker.first_name()
        last_name = faker.last_name()
        position = random.choice(positions)
        team_id = random.randint(1, 32)  # Assuming team IDs range from 1 to 32
        number = random.randint(1, 99)
        height = "{}'{}\"".format(random.randint(5, 6), random.randint(0, 11))  # Example: 5'10"
        weight = random.randint(150, 250)  # Weight in lbs
        dob = faker.date_of_birth(minimum_age=22, maximum_age=40)  # Date of birth between ages 22 and 40
        years_pro = random.randint(0, 22)  # Assuming a range for years pro
        colleges = [
            "University of Alabama",
            "University of Southern California",
            "University of Notre Dame",
            "University of Michigan",
            "Ohio State University",
            "Clemson University",
            "Louisiana State University",
            "University of Florida",
            "Florida State University",
            "University of Texas at Austin",
            "University of Oklahoma",
            "University of Georgia",
            "Penn State University",
            "University of Miami",
            "Auburn University",
            "University of Tennessee",
            "University of Nebraska",
            "Michigan State University",
            "Stanford University",
            "University of Oregon",
            "University of Wisconsin",
            "Texas A&M University",
            "University of Washington",
            "University of Iowa",
            "University of California, Los Angeles"
        ]
        college = random.choice(colleges)  # Randomly select from the list
        photo_url = "avatar{}.png".format(str(id).zfill(2))  # Generates "avatarXX.png"

        FootballPlayer.objects.create(
            id=id,
            first_name=first_name,
            last_name=last_name,
            position=position,
            team=FootballTeam.objects.get_or_create(id=team_id)[0],  # Adjust as necessary for your model
            number=number,
            height=height,
            weight=weight,
            date_of_birth=dob,
            years_pro=years_pro,
            college=college,
            photo_url=photo_url,
        )

# Generate 100 players
generate_players()
