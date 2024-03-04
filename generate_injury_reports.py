import random
from faker import Faker
from datetime import datetime
from api.models import InjuryReportArticle

faker = Faker()

def generate_injury_report_articles(n):
    articles = []
    for _ in range(n):
        id = faker.unique.random_int(min=1, max=10000)
        author = faker.name()
        date = faker.date_time_between(start_date="-1y", end_date="now")
        player_id = random.randint(1, 500)
        title = f"Injury Update: {faker.first_name()} {faker.last_name()}"
        description = f"Update on {title.split(':')[1].strip()}'s condition"
        article_content = faker.text(max_nb_chars=5000)
        image_url = "injury_report_sample.jpg"

        article = InjuryReportArticle(
            id=id,
            author=author,
            date=date,
            player_id=player_id,
            title=title,
            description=description,
            article_content=article_content,
            image_url=image_url
        )
        articles.append(article)

    InjuryReportArticle.objects.bulk_create(articles)

# Generate 10 sample articles
generate_injury_report_articles(10)
