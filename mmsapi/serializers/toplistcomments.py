from rest_framework import serializers
from mmsapi.models import TopListComment
from .mmsusers import MMSUserSerializer

class TopListCommentSerializer(serializers.ModelSerializer):
    user_id = MMSUserSerializer(read_only=True)
    class Meta:
        model = TopListComment
        fields = ("toplist_id", 'user_id', 'text')


class TopListCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopListComment
        fields = ("toplist_id", 'user_id', 'text')