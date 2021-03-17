from rest_framework import serializers
from mmsapi.models import ToWatch
from .medias import MediaSerializer

class ToWatchSerializer(serializers.ModelSerializer):
    media_id = MediaSerializer(read_only=True)
    class Meta:
        model = ToWatch
        
        fields = ('id', 'media_id', 'user_id')


class ToWatchPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToWatch
        
        fields = ('id', 'media_id', 'user_id')