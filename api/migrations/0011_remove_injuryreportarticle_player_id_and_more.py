# Generated by Django 5.0.1 on 2024-03-13 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_season_fga_playerseasonstats_fga_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='injuryreportarticle',
            name='player_id',
        ),
        migrations.AddField(
            model_name='injuryreportarticle',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.footballplayer'),
        ),
    ]
