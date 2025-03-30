# Generated by Django 5.0.3 on 2025-03-29 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_injuryreportarticle_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FantasyDraft',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_teams', models.IntegerField()),
                ('teams_joined', models.IntegerField()),
                ('has_started', models.BooleanField()),
                ('has_finished', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FantasyDraftTeam',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=255)),
                ('draft_position', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('draft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draft_teams', to='api.fantasydraft')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draft_teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FantasyDraftSelection',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pick_number', models.IntegerField()),
                ('draft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draft_selections', to='api.fantasydraft')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='api.footballplayer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draft_selections', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='api.fantasydraftteam')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyPrediction',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('passing_yards', models.IntegerField()),
                ('passing_tds', models.IntegerField()),
                ('passer_rating', models.FloatField()),
                ('ints', models.IntegerField()),
                ('fumbles_lost', models.IntegerField()),
                ('rushing_yards', models.IntegerField()),
                ('rushing_tds', models.IntegerField()),
                ('receptions', models.IntegerField()),
                ('receiving_yards', models.IntegerField()),
                ('receiving_tds', models.IntegerField()),
                ('fgm0_19', models.IntegerField()),
                ('fgm20_39', models.IntegerField()),
                ('fgm40_49', models.IntegerField()),
                ('fgm50_plus', models.IntegerField()),
                ('fga', models.IntegerField()),
                ('xpm', models.IntegerField()),
                ('xpa', models.IntegerField()),
                ('standard_points', models.FloatField()),
                ('ppr_points', models.FloatField()),
                ('half_ppr_points', models.FloatField()),
                ('prediction_comment', models.CharField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_pred', to='api.footballplayer')),
            ],
        ),
    ]
