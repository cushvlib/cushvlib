from django.urls import path
from . import views

urlpatterns = [
    path("", views.episode_list, name="episode_list"),
    path("episodes/<int:episode_id>/", views.episode_detail, name="episode_detail"),
]
