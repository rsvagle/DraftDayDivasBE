# Generated by Django 5.0.1 on 2024-03-10 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_playerseasonstats_delete_playerstats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_fga',
            new_name='fga',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_fgm',
            new_name='fgm',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_fumbles',
            new_name='fumbles',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_fumbles_lost',
            new_name='fumbles_lost',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_ints',
            new_name='ints',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_passer_rating',
            new_name='passer_rating',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_passing_tds',
            new_name='passing_tds',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_passing_yards',
            new_name='passing_yards',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_receiving_tds',
            new_name='receiving_tds',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_receiving_yards',
            new_name='receiving_yards',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_receptions',
            new_name='receptions',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_rushing_tds',
            new_name='rushing_tds',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_rushing_yards',
            new_name='rushing_yards',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_safeties',
            new_name='safeties',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_xpa',
            new_name='xpa',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season_xpm',
            new_name='xpm',
        ),
        migrations.RenameField(
            model_name='playerseasonstats',
            old_name='season',
            new_name='year',
        ),
        migrations.RemoveField(
            model_name='playerseasonstats',
            name='season_fantasy_points',
        ),
    ]
