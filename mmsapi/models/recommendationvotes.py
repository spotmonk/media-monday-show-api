from django.db import models
from django.db.models.deletion import CASCADE


class RecommendationVote(models.Model):
    recommendation_id =  models.ForeignKey("Recommendation",
        on_delete=CASCADE,
        related_name="recommendationvotes",
        related_query_name="recommendationvote")
    user_id = models.ForeignKey("MMSUser",
        on_delete=CASCADE,
        related_name="recommendationvoteusers",
        related_query_name="recommendationvoteuser")
