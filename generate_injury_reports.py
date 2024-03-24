import random
from faker import Faker
from datetime import datetime
from api.models import FootballPlayer, InjuryReportArticle
from django.utils import timezone

faker = Faker()

def generate_injury_report_articles(n):
    articles = []
    for _ in range(n):
        id = faker.unique.random_int(min=1, max=10000)
        author = faker.name()
        naive_date = faker.date_time_between(start_date="-1y", end_date="now")
        date = timezone.make_aware(naive_date)

        player_id = random.randint(1, 250)
        player = FootballPlayer.objects.get(id = player_id)
        title, description = generate_injury_report_title_description(player)

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

def generate_injury_report_title_description(player):
    # List of template pairs (title, description)
    templates = [
        ("Injury Update: {first_name} {last_name}", "An update on {last_name}'s condition."),
        ("Strained Calf: {last_name} doubtful for this week", "{last_name}'s condition will be evaluated at game time."),
        ("{team_name}' {first_name} {last_name} has a broken wrist", "{last_name}'s injury could keep him out multiple weeks."),
        ("Concussion Protocol for {first_name} {last_name}", "{last_name} is undergoing standard concussion protocol, impacting {team_name}'s lineup."),
        ("ACL Concerns: {first_name} {last_name} to miss season", "A devastating blow for {team_name} as {last_name} faces a season-ending ACL injury."),
        ("{first_name} {last_name}, {position}, sidelined with hamstring injury", "{last_name}'s hamstring issue raises concerns for {team_name}'s offensive flexibility."),
        ("{team_name}'s {position} {last_name} suffers ankle sprain", "Questions around {first_name} {last_name}'s availability for the upcoming game linger after injury."),
        ("Back Injury: {first_name} {last_name}'s status uncertain", "{team_name} awaits further tests to determine {last_name}'s playing condition."),
        ("Shoulder Injury Update for {first_name} {last_name}", "{last_name}'s shoulder rehab progressing, optimism for a return this season."),
        ("{team_name} braces for {first_name} {last_name}'s knee recovery", "The road to recovery begins for {last_name}, with hopes high within {team_name}'s camp."),
        ("Foot Injury Sidelines {first_name} {last_name}", "{last_name}'s recent foot injury has the {team_name} reevaluating their strategy."),
        ("Groin Strain Puts {first_name} {last_name} on Week-to-Week Status", "The {team_name} are closely monitoring {last_name}'s recovery from a painful groin strain."),
        ("Rib Injury: {first_name} {last_name} Undergoes Evaluation", "Concerns grow as {last_name}, {team_name}'s {position}, undergoes further tests for a rib injury."),
        ("{first_name} {last_name}'s Thumb Injury: Impact on {team_name}", "With {last_name} nursing a thumb injury, the {team_name}'s passing game might see adjustments."),
        ("Hip Injury: {first_name} {last_name} Faces Weeks of Rehab", "The recovery timeline for {last_name}'s hip injury suggests a challenging few weeks ahead for the {team_name}."),
        ("{team_name} Reports {first_name} {last_name}'s Turf Toe", "{last_name}'s battle with turf toe adds to the {team_name}'s injury woes."),
        ("Dislocated Shoulder Sidelines {first_name} {last_name}", "After a dislocated shoulder, {last_name}'s season with the {team_name} hangs in the balance."),
        ("{first_name} {last_name}'s Torn Pectoral: Surgery and Recovery", "{last_name} faces a long road to recovery after tearing his pectoral, a significant loss for the {team_name}."),
        ("Fractured Jaw: {first_name} {last_name}'s Comeback Trail", "The {team_name}'s {position}, {last_name}, starts his comeback from a serious jaw fracture."),
        ("{first_name} {last_name}'s Calf Strain: Testing Depth for {team_name}", "As {last_name} recovers from a calf strain, the {team_name} looks to their roster depth to fill the void."),
        ("Quad Injury Limits {first_name} {last_name}'s Mobility", "A quad injury has significantly limited {last_name}'s mobility, affecting the {team_name}'s offensive options."),
        ("{first_name} {last_name}'s Elbow Sprain: Awaiting MRI Results", "The {team_name} and {last_name} await MRI results to understand the full extent of his elbow sprain."),
        ("Concussion Concerns for {first_name} {last_name}", "{last_name}'s recent concussion has sparked concern over his long-term health and immediate gameplay for the {team_name}."),
        ("Ligament Tear in {first_name} {last_name}'s Knee Raises Concerns", "A ligament tear in {last_name}'s knee has the {team_name} worried about his future contributions to the team."),
        ("Broken Finger: {first_name} {last_name} Adjusts to Play Through Injury", "{last_name} and the {team_name} are making adjustments for him to play through a broken finger."),
    ]

    # Select a random template pair
    title_template, description_template = random.choice(templates)

    # Format the selected templates with player's name, team name, and position
    title = title_template.format(first_name=player.first_name, last_name=player.last_name, team_name=player.team.team_name, position=player.position)
    description = description_template.format(first_name=player.first_name, last_name=player.last_name, team_name=player.team.team_name, position=player.position)

    return title, description