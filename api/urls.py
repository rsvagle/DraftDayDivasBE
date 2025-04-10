from django.urls import path
from api.views import football_teams_views, auth_views, news_views, mock_draft_views, player_views, stats_views

urlpatterns = [
    # User drafted team
    path('drafted_teams/<int:id>', mock_draft_views.DraftedTeamView.as_view()),

    # News
    path('news/', news_views.NewsArticleListView.as_view()),
    path('news/article/<int:id>', news_views.NewsArticleView.as_view()),
    path('news/player/<int:id>/all/', news_views.PlayerNewsArticlesView.as_view()),

    # Injury reports
    path('injury-report/<int:id>/all/', news_views.AllInjuryReportsForPlayerView.as_view()),
    path('injury-report/', news_views.AllInjuryReportArticlesView.as_view()),
    path('injury-report/<int:id>', news_views.InjuryReportArticleView.as_view()),
    
    # Auth/Registration
    path('login/', auth_views.login),
    path('signup/', auth_views.signup),
    path('test_token/', auth_views.test_token),
    path('profile/', auth_views.get_user_profile),
    path('profile/save_profile/', auth_views.save_user_profile),

    # Teams
    path('teams/', football_teams_views.FootballTeamsView.as_view()),
    path('teams/<int:id>', football_teams_views.SingleFootballTeamView.as_view()),

    path('teams/players/<int:id>', player_views.TeamPlayersListView.as_view()),

    # Players
    path('player/player-summary/<int:id>', player_views.PlayerSummaryView.as_view(), name='player-summary'),
    path('player/with-team-latest-season/<int:id>', player_views.FootballPlayerWithTeamLatestSeasonView.as_view(), name='player-with-team-latest-season'),
    path('player/all-seasons/<int:id>', player_views.FootballPlayerAllSeasonsView.as_view(), name='player-all-seasons'),
    path('players/', player_views.FootballPlayersListView.as_view()),
    
    # Stats based urls
    path('stats/<str:year>', stats_views.GetSeasonStatsListView.as_view()),
    path('stats/search/', stats_views.StatsSearchView.as_view()),
    path('top-performers/', stats_views.GetTopPerformers.as_view()),
    path('rankings/', stats_views.RankingsView.as_view()),
    path('game-logs/<int:player_id>/<str:year>', stats_views.GetPlayerSeasonGameLogsView.as_view()),
    path('game-logs/<int:player_id>/recent/', stats_views.GetPlayerRecentGameLogsView.as_view()),

    # Mock drafts
    path('mock-draft/', mock_draft_views.FantasyDraftListCreateView.as_view()),
    path('mock-draft/join', mock_draft_views.FantasyDraftJoinView.as_view()),
    path('mock-draft/joined/', mock_draft_views.MyJoinedDraftsView.as_view(), name='my-joined-drafts'),
    
    # Select player
    # Get results
    # Get mock draft setup
    
]
