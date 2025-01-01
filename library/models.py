from django.db import models

from django.db import models

class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Sentence(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='sentences')
    text = models.TextField()
    start_time = models.FloatField()  # Start time in seconds
    end_time = models.FloatField()  # End time in seconds

    def __str__(self):
        return f"{self.episode.title} - {self.start_time:.2f}s"
