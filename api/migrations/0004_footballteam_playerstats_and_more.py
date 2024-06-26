# Generated by Django 5.0.1 on 2024-01-27 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_newsarticle_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='FootballTeam',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(default='', max_length=60)),
                ('location', models.CharField(default='', max_length=100)),
                ('coach', models.CharField(default='', max_length=100)),
                ('stadium', models.CharField(default='', max_length=100)),
                ('founded_year', models.IntegerField(blank=True, null=True)),
                ('championships_won', models.IntegerField(default=0)),
                ('logo_url', models.URLField(default='')),
                ('official_website_url', models.URLField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('player_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='draftedteam',
            old_name='teamName',
            new_name='team_name',
        ),
        migrations.RenameField(
            model_name='draftedteam',
            old_name='userID',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='FootballPlayer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=60)),
                ('last_name', models.CharField(default='', max_length=60)),
                ('position', models.CharField(default='', max_length=30)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('height', models.CharField(default='', max_length=10)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('years_pro', models.IntegerField(default=0)),
                ('college', models.CharField(blank=True, default='', max_length=100)),
                ('photo_url', models.URLField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.footballteam')),
            ],
        ),
    ]
