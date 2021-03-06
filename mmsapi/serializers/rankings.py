from rest_frammework import serializers
from mmsapi.models import Ranking

class RankingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ('ranking', 'media_id', 'user_id')
