from django.urls import path
from .views import PlayerSummaryView, main, players, DraftedTeamView, NewsArticleView
from api import views

urlpatterns = [
    path('home', main),
    path('players/', players),
    path('drafted_teams/', DraftedTeamView.as_view()),
    path('news/', NewsArticleView.as_view()),
    path('player/player-summary/<int:id>', PlayerSummaryView.as_view(), name='player-summary'),
    path('login/', views.login),
    path('signup/', views.signup),
    path('test_token/', views.test_token),
    path('profile/', views.get_user_profile),
    path('save_profile/', views.save_user_profile),
]
