from django.contrib import admin
from .models import InjuryReportArticle, NewsArticle, FootballPlayer, FootballTeam, PlayerGameLog, PlayerSeasonStats

# Register your models here.
admin.site.register(NewsArticle)
admin.site.register(FootballPlayer)
admin.site.register(FootballTeam)
admin.site.register(InjuryReportArticle)
admin.site.register(PlayerSeasonStats)
admin.site.register(PlayerGameLog)