from django.db import models
from django.db.models.deletion import CASCADE

class Recommendation(models.Model):
    media_id = models.ForeignKey("Media",
        on_delete=CASCADE,
        related_name="recommendations",
        related_query_name="recommendation")
