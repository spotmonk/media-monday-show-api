from django.db import models

class Episode(models.Model):
    title = models.CharField(max_length=200)
    blurb = models.TextField()
    host_comments = models.TextField()
    start_date = models.DateField()
    url = models.TextField(unique=True)
    episode_type = models.CharField(max_length=50, null=True)
