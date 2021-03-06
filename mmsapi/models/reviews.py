from django.db import models
from django.db.models.deletion import CASCADE

class Review(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    media_id =  models.ForeignKey("Media",
        on_delete=CASCADE,
        related_name="mediareviews",
        related_query_name="mediareview")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="reviewusers",
        related_query_name="reviewuser")
