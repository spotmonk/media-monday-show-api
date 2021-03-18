from rest_framework import serializers
from mmsapi.models import ReviewComment
from .mmsusers import MMSUserSerializer

class ReviewCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = ("review_id", 'user_id', 'text')


class ReviewCommentSerializer(serializers.ModelSerializer):
    user_id = MMSUserSerializer(read_only=True)
    class Meta:
        model = ReviewComment
        fields = ("review_id", 'user_id', 'text')
