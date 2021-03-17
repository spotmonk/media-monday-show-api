from rest_framework import serializers
from mmsapi.models import Watched
from .medias import MediaSerializer

class WatchedSerializer(serializers.ModelSerializer):
    media_id = MediaSerializer(read_only=True)

    class Meta:
        model = Watched
        fields = ('id', 'media_id', 'user_id', 'date_watched', 'rating', 'prating')


class ToWatchPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watched
        
        fields = ('id', 'media_id', 'user_id', 'date_watched', 'rating', 'prating')