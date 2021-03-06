from django.db import models
from django.db.models.deletion import CASCADE

class HostRecommendation(models.Model):
    episode_id =  models.ForeignKey("Episode",
        on_delete=CASCADE,
        related_name="episoderecommendations",
        related_query_name="episoderecommendation")
    media_id =  models.ForeignKey("Media",
        on_delete=CASCADE,
        related_name="recommendationmedia",
        related_query_name="recommendationmedia")
