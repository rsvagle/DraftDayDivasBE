import random
from faker import Faker
from datetime import datetime
from api.models import FootballPlayer, InjuryReportArticle

faker = Faker()

def generate_injury_report_articles(n):
    articles = []
    for _ in range(n):
        id = faker.unique.random_int(min=1, max=10000)
        author = faker.name()
        date = faker.date_time_between(start_date="-1y", end_date="now")
        player_id = random.randint(1, 150)

        player = FootballPlayer.objects.get(id = player_id)

        title = f"Injury Update: {player.first_name} {player.last_name}"
        description = f"Update on {player.last_name}'s condition"
        article_content = faker.text(max_nb_chars=5000)
        image_url = player.photo_url

        article = InjuryReportArticle(
            id=id,
            author=author,
            date=date,
            player=player,
            title=title,
            description=description,
            article_content=article_content,
            image_url=image_url
        )
        articles.append(article)

    InjuryReportArticle.objects.bulk_create(articles)

