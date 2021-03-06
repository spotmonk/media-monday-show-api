from rest_framework import serializers
from mmsapi.models import Watched
from .medias import MediaSerializer

class WatchedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watched
        media_id = MediaSerializer(read_only=True)
        fields = ('media_id', 'user_id', 'date', 'rating', 'prating')
