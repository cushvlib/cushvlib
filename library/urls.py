from django.urls import path
from . import views

urlpatterns = [
    path('', views.episode_list, name='episode_list'),
]
