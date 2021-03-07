from rest_framework import serializers
from mmsapi.models import Ranking

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ('ranking', 'media_id', 'user_id')
