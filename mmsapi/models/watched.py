from django.db import models
from django.db.models.deletion import CASCADE

class Watched(models.Model):
    media_id =  models.ForeignKey("Media",
        on_delete=CASCADE,
        related_name="mediawatcheds",
        related_query_name="mediawatched")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="watchedusers",
        related_query_name="watcheduser")
    date_watched = models.DateField(auto_now_add=True)
    rating = models.IntegerField(null=True)
    prating = models.IntegerField(null=True)
