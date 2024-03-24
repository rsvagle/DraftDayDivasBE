import random
from faker import Faker
from datetime import datetime
from api.models import FootballPlayer, NewsArticle
from django.utils import timezone

faker = Faker()

def generate_news_articles(n):
    articles = []
    for i in range(n):
        id = faker.unique.random_int(min=1, max=10000)
        author = faker.name()
        naive_date = faker.date_time_between(start_date="-2y", end_date="now")
        date = timezone.make_aware(naive_date)

        player_id = random.randint(1, 150)
        player = FootballPlayer.objects.get(id = player_id)

        title, description = generate_news_title_description(player)
        
        article_content = faker.text(max_nb_chars=5000)
        image_url = "news-image-{}.jpg".format(str(i))

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
        ("{last_name}'s Arm Strength Rewrites Game Plan", "QB {first_name} {last_name} showcased a cannon for an arm, altering {team_name}'s offensive strategy."),
        ("Vision and Precision: {first_name} {last_name}'s Winning Formula", "The quarterback's impeccable vision and precision passing led {team_name} to victory."),
        ("{first_name} {last_name} Escapes Pressure, Delivers Victory", "Under immense pressure, {last_name} maneuvered skillfully to lead {team_name} to a thrilling win."),
        ("QB {last_name} Tackles Record Books", "{first_name} {last_name} etched his name in the record books with another stellar performance."),
        ("{last_name}'s Touchdown Gala Electrifies {team_name}", "Quarterback {first_name} {last_name}'s multiple touchdowns electrified the stadium."),
        ("The Comeback Kid: {first_name} {last_name}", "{last_name}'s ability to rally {team_name} from behind cemented his status as the comeback kid."),
        ("Dual-Threat {last_name} Confounds Defense", "{first_name} {last_name}, a dual-threat QB, left the defense guessing and led {team_name} to a win."),
        ("{first_name} {last_name}: Clutch Performer When It Counts", "{last_name}'s clutch performances in critical moments have become the talk of the league."),
        ("{last_name}'s Leadership Fuels {team_name}'s Ascent", "The leadership qualities of QB {first_name} {last_name} are a key factor in {team_name}'s success."),
        ("Game Manager to Game Winner: {first_name} {last_name}'s Evolution", "{last_name}'s evolution from game manager to game winner has been remarkable."),
    ]

    rb_templates = [
        ("{last_name} Runs Wild Against Defenses", "RB {first_name} {last_name} racked up yards, showcasing his elite talent."),
        ("Ground Game Guru: {first_name} {last_name}'s Big Day", "{last_name} was unstoppable, powering {team_name} to a ground-and-pound victory."),
        ("{last_name}'s Rushing Brilliance Lights Up the League", "{first_name} {last_name}'s performance set the tone for a commanding {team_name} win."),
        ("{last_name}: A Force Between the Tackles", "RB {first_name} {last_name} proved unstoppable between the tackles, bolstering {team_name}'s ground game."),
        ("Versatile {last_name} Powers Through Defense", "{first_name} {last_name}'s versatility was on full display as he powered through the defense."),
        ("Breakaway Speed: {last_name}'s Signature", "{first_name} {last_name}'s breakaway speed turned heads and broke defenses apart."),
        ("{last_name}'s Yards After Contact Impress", "RB {first_name} {last_name}'s yards after contact were a testament to his toughness and skill."),
        ("{first_name} {last_name} Sets Rushing Record", "With an historic rushing performance, {last_name} set a new benchmark for future backs."),
        ("The Bulldozer: {first_name} {last_name}'s Dominant Game", "RB {first_name} {last_name}, known as 'The Bulldozer,' left his mark on the game with a dominant performance."),
        ("{last_name} Catches, Runs, and Scores", "Showing off his dual-threat capability, {last_name} contributed in all facets of the offense."),
        ("Endurance and Power: {last_name}'s Winning Combo", "{first_name} {last_name}'s mix of endurance and power was too much for the opposition."),
        ("{last_name}'s Agility Lights Up the Field", "RB {first_name} {last_name}'s agility and footwork were a spectacle, leaving defenders in his wake."),
        ("Goal-Line Specialist {last_name} Strikes Again", "RB {first_name} {last_name}, the goal-line specialist, delivered crucial touchdowns for {team_name}."),
    ]

    wr_templates = [
        ("{last_name} Soars to New Heights", "WR {first_name} {last_name} made highlight-reel catches, amassing yards and touchdowns."),
        ("Record-Breaking Day for {first_name} {last_name}", "{last_name}'s hands were magnets, as he broke the single-game receiving yards record."),
        ("The Unstoppable {first_name} {last_name}", "No cornerback could hold back {last_name}, who lit up the scoreboard for {team_name}."),
        ("{last_name}'s Route Running Precision", "WR {first_name} {last_name} showcased masterful route running, leaving defenders behind."),
        ("Air {last_name}: Sky-High Catches Seal the Game", "{first_name} {last_name}'s ability to make sky-high catches sealed the game for {team_name}."),
        ("{first_name} {last_name}: Yards After Catch Phenom", "{last_name}'s yards after catch (YAC) turned short passes into big gains."),
        ("Deep Threat {last_name} Stretches the Field", "WR {first_name} {last_name}, the ultimate deep threat, stretched the field and terrorized the secondary."),
        ("{last_name} Breaks Loose for Career-High Yards", "WR {first_name} {last_name} broke loose, setting a new career-high in receiving yards."),
        ("{last_name}'s Sideline Acrobatics Stun Fans", "WR {first_name} {last_name}'s acrobatic catches along the sidelines captivated fans and secured key first downs."),
        ("{first_name} {last_name} Overpowers Defenders in Air", "{last_name} used his superior size and strength to overpower defenders for critical catches."),
        ("Slot Magician {last_name} Dazzles in the Middle", "Operating from the slot, {first_name} {last_name} found seams in the defense, turning short grabs into significant gains."),
        ("{last_name}'s Two-Touchdown Performance", "WR {first_name} {last_name} found the end zone twice, proving pivotal in {team_name}'s offensive onslaught."),
        ("Return Specialist {last_name} Changes the Game", "Beyond receiving, {first_name} {last_name}'s impact as a return specialist swung momentum in {team_name}'s favor."),
    ]

    te_templates = [
        ("{first_name} {last_name}: Red Zone Monster", "{last_name}'s knack for finding the end zone was on full display in a thrilling {team_name} victory."),
        ("Tight End {last_name} Dominates Middle of the Field", "With unmatched physicality and skill, {first_name} {last_name} was the game's standout performer."),
        ("{last_name}'s Dual-Threat Performance", "TE {first_name} {last_name} excelled in blocking and receiving, pivotal to {team_name}'s offensive strategy."),
        ("{last_name} Breaks Tackles, Scores Game-Winner", "TE {first_name} {last_name}'s ability to break tackles led to the game-winning touchdown for {team_name}."),
        ("Blocking Beast {last_name} Paves the Way", "{first_name} {last_name} showcased his blocking prowess, paving the way for {team_name}'s ground game."),
        ("{first_name} {last_name}: The Unsung Hero in {team_name} Victory", "TE {first_name} {last_name}'s all-around play proved to be the unsung hero in a tight victory."),
        ("The Safety Valve: {first_name} {last_name} Comes Through", "When the offense needed a spark, TE {first_name} {last_name} was the reliable safety valve."),
        ("{last_name}'s Career Day Highlights Versatility", "A career-best performance from TE {first_name} {last_name} showcased his versatility and vital role."),
        ("Red Zone Threat: {first_name} {last_name} Unstoppable", "In the red zone, TE {first_name} {last_name} was simply unstoppable, adding another touchdown to his tally."),
        ("{last_name}'s Clutch Catches Keep Drives Alive", "Critical third-down conversions by TE {first_name} {last_name} kept pivotal drives alive."),
        ("{first_name} {last_name}: A Nightmare Matchup", "Defenses struggled to contain TE {first_name} {last_name}, a nightmare matchup across the middle."),
        ("{last_name} Showcases Elite Route Running", "With elite route running, TE {first_name} {last_name} created separation and racked up yards."),
        ("The Go-To Guy: {first_name} {last_name}'s Key Role", "As {team_name}'s go-to guy, TE {first_name} {last_name} delivered in moments big and small."),
    ]

    k_templates = [
        ("{last_name} Kicks {team_name} to Glory", "The leg of K {first_name} {last_name} was the difference, nailing crucial field goals."),
        ("Clutch Kicker {first_name} {last_name} Seals the Deal", "{last_name}'s game-winning field goal as time expired will be remembered for ages."),
        ("{last_name}: From Unsung Hero to Headliner", "With pinpoint accuracy, K {first_name} {last_name} scored all of {team_name}'s points."),
        ("{last_name} Delivers Under Pressure", "In a display of nerves of steel, K {first_name} {last_name} delivered the winning kick under immense pressure."),
        ("The Ice Man: {first_name} {last_name} Stays Cool", "K {first_name} {last_name}, known as 'The Ice Man,' stayed cool to kick the crucial field goals."),
        ("{last_name}'s Leg Powers {team_name} to Win", "With a powerful leg, K {first_name} {last_name} contributed mightily to {team_name}'s victory."),
        ("Distance and Accuracy: {last_name}'s Winning Combo", "K {first_name} {last_name} showcased both distance and accuracy, a winning combo for {team_name}."),
        ("Record-Setting Day for Kicker {last_name}", "K {first_name} {last_name} had a record-setting day, etching his name in the history books."),
        ("{first_name} {last_name}: The Hero in Cleats", "When all seemed lost, K {first_name} {last_name}, the hero in cleats, stepped up to secure the win."),
        ("{last_name}'s Perfect Game Keeps {team_name} Undefeated", "K {first_name} {last_name}'s perfect kicking game was key in keeping {team_name}'s undefeated streak alive."),
        ("From Doubtful to Decisive: {last_name}'s Journey", "Once considered the team's Achilles heel, K {first_name} {last_name} proved decisive, turning skeptics into believers."),
        ("{last_name} Splits the Uprights in Overtime", "With the game on the line in overtime, K {first_name} {last_name} calmly split the uprights, sealing a thrilling victory."),
        ("Wind-Defying Kick by {last_name} Astounds", "Despite challenging winds, K {first_name} {last_name} astounded everyone with a wind-defying kick that sailed through."),
        ("The Redemption of Kicker {first_name} {last_name}", "After a tough start to the season, K {first_name} {last_name}'s redemption came with a game-winning kick."),
        ("{last_name}'s Consistency Key for {team_name}", "The consistency of K {first_name} {last_name} has become a key asset for {team_name}, contributing to their success."),
        ("Rookie {last_name} Makes the Cut with Historic Kick", "Rookie K {first_name} {last_name} made an immediate impact with a historic kick, securing his spot in the team."),
        ("{last_name} Rewrites Game with Punt Precision", "Not just a placekicker, {first_name} {last_name}'s precision in punting changed the field position game."),
    ]

    team_templates = [
        ("Gritty {team_name} Outlast Their Opponents", "{last_name}'s heroics in overtime clinched the victory"),
        ("{team_name} Defense Stifles Rivals", "A collective effort led by the defensive line shut down the opposition."),
        ("Special Teams Spark {team_name} Victory", "Key plays from the special teams unit, including a punt return touchdown, were crucial for the win."),
        ("{team_name}'s Comeback Stuns the League", "Down but never out, {team_name} orchestrated a comeback for the ages, led by {position} {last_name}."),
        ("{team_name} Shatters Expectations with Dominant Win", "An all-around masterclass saw {team_name} dismantle their opponents in a highly anticipated matchup."),
        ("Historic Victory: {team_name} Sets New Records", "With a performance for the ages, {team_name} set new league records in their latest win."),
        ("{team_name} Shows Championship Mettle in Tough Win", "Fighting through adversity, {team_name} displayed their championship credentials in a hard-fought victory."),
        ("Rookie Sensations Lead {team_name} to Victory", "The young guns of {team_name} stepped up, contributing significantly to a crucial win."),
        ("{team_name}'s Balanced Attack Overwhelms Opponents", "A potent mix of rushing and passing led {team_name} to a commanding victory."),
        ("Defensive Masterpiece: {team_name} Shuts Out Rivals", "{team_name}'s defense was impenetrable, recording a rare shutout against their rivals."),
        ("{team_name} Capitalizes on Turnovers for Win", "A relentless {team_name} took advantage of every turnover, converting mistakes into points for a decisive victory."),
        ("Unstoppable {team_name} Extend Winning Streak", "With another win, {team_name} extends their winning streak, eyeing the playoffs with confidence."),
        ("{team_name}'s Ground Game Runs Rampant", "Dominating the trenches, {team_name}'s rushing attack was too much for the opposition to handle."),
        ("{team_name} Overcomes Injuries to Secure Victory", "Despite key injuries, {team_name} rallied together to claim a hard-earned win."),
        ("{team_name}'s Late Rally Falls Short in Thriller", "A valiant comeback attempt by {team_name} came up just short in a game that had fans on the edge of their seats."),
        ("{team_name}'s Offensive Fireworks Light Up the Sky", "With an explosive offensive display, {team_name} lit up the scoreboard in a high-scoring affair."),
        ("Suffocating {team_name} Defense Clamps Down in the Clutch", "When it mattered most, {team_name}'s defense tightened the noose, securing a pivotal win."),
        ("Special Teams Blunder Costs {team_name} Dearly", "A rare mistake by the special teams unit turned the tide against {team_name} in a closely contested battle."),
        ("{team_name} Coasts to Easy Victory Amidst Rivalry Game", "In a highly anticipated rivalry game, {team_name} made a statement with a dominant performance."),
        ("{team_name} Stunned at Home by Underdog", "In an unexpected turn of events, {team_name} fell to an underdog, shaking up the standings."),
        ("Record-Breaking Performance Propels {team_name} to Win", "{team_name} rode a record-breaking performance to a commanding victory, marking a memorable day."),
        ("{team_name} Faces Setback as Star Player Sidelined", "With their star player sidelined, {team_name} faced a tough challenge but showed resilience in adversity."),
        ("{team_name} Clinches Playoff Spot with Decisive Win", "Securing their place in the playoffs, {team_name} left no doubts with a decisive victory over their rivals."),
        ("Weather Woes: {team_name} Battles Elements and Opponents", "Facing not just their opponents but adverse weather conditions, {team_name} showed their mettle in a gritty win."),
        ("{team_name}'s Perfect Season Continues Unabated", "Defying odds and expectations, {team_name} marches on, keeping their perfect season alive."),
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