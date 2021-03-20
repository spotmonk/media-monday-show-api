from rest_framework import serializers
from mmsapi.models import Ranking
from .medias import MediaSerializer

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ('id', 'ranking', 'media_id', 'user_id')

class RankingReadSerializer(serializers.ModelSerializer):
    media_id = MediaSerializer(read_only=True)
    class Meta:
        model=Ranking
        fields = ('id', 'ranking', 'media_id', 'user_id')