from django.db import models
from django.db.models.deletion import CASCADE

class Ranking(models.Model):
    ranking = models.IntegerField()
    media_id =  models.ForeignKey("Media",
        on_delete=CASCADE,
        related_name="mediarankings",
        related_query_name="mediaranking")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="rankingusers",
        related_query_name="rankinguser")
