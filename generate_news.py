import random
from faker import Faker
from datetime import datetime
from api.models import NewsArticle

faker = Faker()

def generate_news_articles(n):
    articles = []
    for _ in range(n):
        id = faker.unique.random_int(min=1, max=10000)
        author = faker.name()
        date = faker.date_time_between(start_date="-1y", end_date="now")
        title = faker.paragraph(nb_sentences=1)
        description = faker.paragraph(nb_sentences=1)
        article_content = faker.text(max_nb_chars=5000)
        image_url = "news_article_sample.jpg"

        article = NewsArticle(
            id=id,
            author=author,
            date=date,
            title=title,
            description=description,
            article_content=article_content,
            image_url=image_url
        )
        articles.append(article)

    NewsArticle.objects.bulk_create(articles)

# Generate 10 sample articles
generate_news_articles(5)
