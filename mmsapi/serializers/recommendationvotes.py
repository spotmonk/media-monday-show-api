from rest_frammework import serializers
from mmsapi.models import RecommendationVote

class RecomendationVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationVote
        fields = ('recommendation_id', 'user_id')
