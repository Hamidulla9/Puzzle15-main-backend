from django.urls import path
from .views import SubmitScoreAPIView, LeaderboardAPIView

urlpatterns = [
    path('submit-score/', SubmitScoreAPIView.as_view(), name='submit-score'),
    path('leaderboard/', LeaderboardAPIView.as_view(), name='leaderboard'),
]
