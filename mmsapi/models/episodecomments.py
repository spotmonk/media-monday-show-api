from django.db import models
from django.db.models.deletion import CASCADE

class EpisodeComment(models.Model):
    episode_id =  models.ForeignKey("Episode",
        on_delete=CASCADE,
        related_name="episodecomments",
        related_query_name="episodecomment")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="episodecommentusers",
        related_query_name="episodecommentuser")
    text = models.TextField()
