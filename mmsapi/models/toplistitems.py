from django.db import models
from django.db.models.deletion import CASCADE

class TopListItem(models.Model):
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="toplistitemusers",
        related_query_name="toplistitemuser")
    ranking = models.IntegerField()
    media_id =  models.ForeignKey("Media",
        on_delete=CASCADE,
        related_name="toplistitemmedia",
        related_query_name="itemmedia")
    