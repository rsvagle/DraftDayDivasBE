import math
import random
from faker import Faker
from datetime import datetime

import numpy as np
from api.models import FootballPlayer, FootballTeam, NewsArticle

faker = Faker()

def generate_players():
    positions = ["QB", "RB", "WR", "TE", "K"]
    positions_no_k = ["RB", "WR", "TE"]
    id_index = 1
    teams = FootballTeam.objects.all()

    for team in teams:
        for position in positions:
            id=id_index
            first_name = faker.first_name_male()
            last_name = faker.last_name()
            position = position
            number = random.randint(1, 99)
            height = "{}'{}\"".format(random.randint(5, 6), random.randint(0, 11))  # Example: 5'10"
            weight = random.randint(150, 250)  # Weight in lbs
            random_age = min(40,max(23,math.floor(np.random.normal(28, 6, 1))))
            dob = faker.date_of_birth(minimum_age=random_age, maximum_age=random_age)
            years_pro = max(1,(2024 - dob.year) - random.randint(21, 23))  # Assuming a range for years pro
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
                team=team,
                number=number,
                height=height,
                weight=weight,
                date_of_birth=dob,
                years_pro=years_pro,
                college=college,
                photo_url=photo_url,
            )

            id_index += 1

    for team in teams:
        for id in range(1, 4):
            id=id_index
            first_name = faker.first_name_male()
            last_name = faker.last_name()
            position = random.choice(positions_no_k)
            team_id = random.randint(1, 32)  # Assuming team IDs range from 1 to 32
            number = random.randint(1, 99)
            height = "{}'{}\"".format(random.randint(5, 6), random.randint(0, 11))  # Example: 5'10"
            weight = random.randint(150, 250)  # Weight in lbs
            random_age = min(40,max(22,math.floor(np.random.normal(27, 4, 1))))
            dob = faker.date_of_birth(minimum_age=random_age, maximum_age=random_age)
            years_pro = max(1,(2024 - dob.year) - random.randint(21, 23))  # Assuming a range for years pro
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
                team=teams[team_id-1],
                number=number,
                height=height,
                weight=weight,
                date_of_birth=dob,
                years_pro=years_pro,
                college=college,
                photo_url=photo_url,
            )

            id_index += 1
        
