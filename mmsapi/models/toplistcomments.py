from django.db import models
from django.db.models.deletion import CASCADE

class TopListComment(models.Model):
    toplist_id =  models.ForeignKey("Toplist",
        on_delete=CASCADE,
        related_name="toplistcomments",
        related_query_name="toplistcomment")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="toplistcommentusers",
        related_query_name="toplistcommentuser")
    text = models.TextField()
