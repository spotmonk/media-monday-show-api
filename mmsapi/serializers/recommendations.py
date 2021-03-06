from rest_frammework import serializers
from mmsapi.models import Recommendation

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('media_id')
