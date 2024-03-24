import random
from faker import Faker
from datetime import datetime
from api.models import FootballPlayer, NewsArticle
from django.utils import timezone

faker = Faker()

def generate_news_articles(n):
    articles = []
    for _ in range(n):
        id = faker.unique.random_int(min=1, max=10000)
        author = faker.name()
        naive_date = faker.date_time_between(start_date="-1y", end_date="now")
        date = timezone.make_aware(naive_date)

        player_id = random.randint(1, 150)
        player = FootballPlayer.objects.get(id = player_id)
        title, description = generate_news_title_description(player)
        
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


def generate_news_title_description(player):
    # List of template pairs (title, description)
    qb_templates = [
        ("Quarterback {last_name} Shatters Records", "{first_name} {last_name} set a new league record for passing yards in a single game."),
        ("{last_name}'s Last-Minute Heroics Seal Victory", "In a breathtaking finish, QB {first_name} {last_name}'s precision pass clinched the win."),
        ("{first_name} {last_name}: A Masterclass in Quarterbacking", "{last_name} dazzled with both his arm and his feet, leading {team_name} to a dominant win."),
    ]

    rb_templates = [
        ("{last_name} Runs Wild Against Defenses", "RB {first_name} {last_name} racked up yards, showcasing his elite talent."),
        ("Ground Game Guru: {first_name} {last_name}'s Big Day", "{last_name} was unstoppable, powering {team_name} to a ground-and-pound victory."),
        ("{last_name}'s Rushing Brilliance Lights Up the League", "{first_name} {last_name}'s performance set the tone for a commanding {team_name} win."),
    ]

    wr_templates = [
        ("{last_name} Soars to New Heights", "WR {first_name} {last_name} made highlight-reel catches, amassing yards and touchdowns."),
        ("Record-Breaking Day for {first_name} {last_name}", "{last_name}'s hands were magnets, as he broke the single-game receiving yards record."),
        ("The Unstoppable {first_name} {last_name}", "No cornerback could hold back {last_name}, who lit up the scoreboard for {team_name}."),
    ]

    te_templates = [
        ("{first_name} {last_name}: Red Zone Monster", "{last_name}'s knack for finding the end zone was on full display in a thrilling {team_name} victory."),
        ("Tight End {last_name} Dominates Middle of the Field", "With unmatched physicality and skill, {first_name} {last_name} was the game's standout performer."),
        ("{last_name}'s Dual-Threat Performance", "TE {first_name} {last_name} excelled in blocking and receiving, pivotal to {team_name}'s offensive strategy."),
    ]

    k_templates = [
        ("{last_name} Kicks {team_name} to Glory", "The leg of K {first_name} {last_name} was the difference, nailing crucial field goals."),
        ("Clutch Kicker {first_name} {last_name} Seals the Deal", "{last_name}'s game-winning field goal as time expired will be remembered for ages."),
        ("{last_name}: From Unsung Hero to Headliner", "With pinpoint accuracy, K {first_name} {last_name} scored all of {team_name}'s points."),
    ]

    team_templates = [
        ("Gritty {team_name} Outlast Their Opponents", "{last_name}'s heroics in overtime clinched the victory"),
        ("{team_name} Defense Stifles Rivals", "A collective effort led by the defensive line shut down the opposition."),
        ("Special Teams Spark {team_name} Victory", "Key plays from the special teams unit, including a punt return touchdown, were crucial for the win."),
        ("{team_name}'s Comeback Stuns the League", "Down but never out, {team_name} orchestrated a comeback for the ages, led by {position} {last_name}."),
    ]

    # Select a random template pair (1/3 should be team articles)
    if(random.randint(0,2) < 1):
        title_template, description_template = random.choice(team_templates)
    else:
        match player.position:
            case "QB":
                title_template, description_template = random.choice(qb_templates)
            case "RB":
                title_template, description_template = random.choice(rb_templates)
            case "WR":                
                title_template, description_template = random.choice(wr_templates)
            case "TE":
                title_template, description_template = random.choice(te_templates)
            case "K":
                title_template, description_template = random.choice(k_templates)
            case _:
                pass


    # Format the selected templates with player's name, team name, and position
    title = title_template.format(first_name=player.first_name, last_name=player.last_name, team_name=player.team.team_name, position=player.position)
    description = description_template.format(first_name=player.first_name, last_name=player.last_name, team_name=player.team.team_name, position=player.position)

    return title, description