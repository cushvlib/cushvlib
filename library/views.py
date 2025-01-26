from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Episode, Sentence

def episode_list(request):
    query = request.GET.get("q")
    matching_sentences = []
    episodes = Episode.objects.all()

    if query:
        # Find matching sentences
        matching_sentences = Sentence.objects.filter(text__icontains=query)
        # Filter episodes containing those sentences
        episodes = Episode.objects.filter(sentences__in=matching_sentences).distinct()

    # Generate links for each sentence to the correct episode page
    for sentence in matching_sentences:
        sentence.link = f"{reverse('episode_detail', args=[sentence.episode.id])}#sentence-{sentence.id}"

    return render(request, "library/episode_list.html", {
        "episodes": episodes,
        "query": query,
        "matching_sentences": matching_sentences,
    })

from django.shortcuts import render, get_object_or_404
from .models import Episode

def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id)
    sentences = episode.sentences.all()  # Fetch all sentences related to this episode
    return render(request, "library/episode_detail.html", {"episode": episode, "sentences": sentences})
