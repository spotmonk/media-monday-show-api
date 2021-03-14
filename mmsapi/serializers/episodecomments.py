from rest_framework import serializers
from mmsapi.models import EpisodeComment

class EpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeComment
        fields = ("id", "episode_id", 'user_id', 'text')
