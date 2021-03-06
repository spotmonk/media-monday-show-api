from rest_framework import serializers
from mmsapi.models import ReviewComment

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = ("review_id", 'user_id', 'text')
