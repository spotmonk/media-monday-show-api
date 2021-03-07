from rest_framework import serializers
from mmsapi.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'text', 'media_id', 'user_id')
