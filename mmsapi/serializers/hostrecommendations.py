from rest_framework import serializers
from mmsapi.models import HostRecommendation

class HostRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostRecommendation
        fields = ("episode_id", 'media_id')
