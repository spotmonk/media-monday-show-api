from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_url = models.TextField()
    release_date = models.DateField()
    media_type = models.CharField(max_length=50)
    external_id = models.IntegerField()
