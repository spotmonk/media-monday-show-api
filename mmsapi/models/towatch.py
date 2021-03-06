from django.db import models
from django.db.models.deletion import CASCADE

class ToWatch(models.Model):
    media_id =  models.ForeignKey("Media",
        on_delete=CASCADE,
        related_name="mediatowatchs",
        related_query_name="mediatowatch")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="towatchusers",
        related_query_name="towatchuser")
    date_added = models.DateField()
