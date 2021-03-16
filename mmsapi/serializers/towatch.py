from rest_framework import serializers
from mmsapi.models import ToWatch
from .medias import MediaSerializer

class ToWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToWatch
        media_id = MediaSerializer(read_only=True)
        fields = ('id', 'media_id', 'user_id')
