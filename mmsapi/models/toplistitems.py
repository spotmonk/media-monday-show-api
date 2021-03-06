from django.db import models
from django.db.models.deletion import CASCADE

class TopListItem(models.Model):
    toplist_id =  models.ForeignKey("Toplist",
        on_delete=CASCADE,
        related_name="toplistitems",
        related_query_name="toplistitem")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="toplistitemusers",
        related_query_name="toplistitemuser")
    ranking = models.IntegerField()
