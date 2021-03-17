from rest_framework import serializers
from mmsapi.models import Review
from .mmsusers import MMSUserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user_id = MMSUserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'title', 'text', 'media_id', 'user_id')


class ReviewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'text', 'media_id', 'user_id')
