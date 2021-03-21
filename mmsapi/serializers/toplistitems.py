from rest_framework import serializers
from mmsapi.models import TopListItem
from .medias import MediaSerializer

class TopListItemSerializer(serializers.ModelSerializer):
    media_id = MediaSerializer(read_only=True)
    class Meta:
        model = TopListItem
        fields = ('id', 'user_id', 'ranking', 'media_id')


class TopListItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopListItem
        fields = ('id', 'user_id', 'ranking', 'media_id')
