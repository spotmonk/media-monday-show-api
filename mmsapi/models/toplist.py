from django.db import models
from django.db.models.deletion import CASCADE

class Toplist(models.Model):
    title = models.CharField(max_length=400)
    date = models.DateField()
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="toplistusers",
        related_query_name="toplistuser")
