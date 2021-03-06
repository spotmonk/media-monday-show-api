from django.db import models
from django.db.models.deletion import CASCADE

class ReviewComment(models.Model):
    review_id =  models.ForeignKey("Review",
        on_delete=CASCADE,
        related_name="reviewcomments",
        related_query_name="reviewcomment")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="reviewcommentusers",
        related_query_name="reviewcommentuser")
    text = models.TextField()
