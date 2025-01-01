from django.shortcuts import render
from .models import Episode

def episode_list(request):
    episodes = Episode.objects.all()
    return render(request, 'library/episode_list.html', {'episodes': episodes})
