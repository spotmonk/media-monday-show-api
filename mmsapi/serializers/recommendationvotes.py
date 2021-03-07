from rest_framework import serializers
from mmsapi.models import RecommendationVote

class RecommendationVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationVote
        fields = ('recommendation_id', 'user_id')
