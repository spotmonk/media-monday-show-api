from rest_framework import serializers
from mmsapi.models import EpisodeComment
from .mmsusers import MMSUserSerializer

class EpisodeCommentSerializer(serializers.ModelSerializer):
    user_id = MMSUserSerializer(read_only=True)
    class Meta:
        model = EpisodeComment
        fields = ("id", "episode_id", 'user_id', 'text')


class EpisodeCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeComment
        fields = ("id", "episode_id", 'user_id', 'text')