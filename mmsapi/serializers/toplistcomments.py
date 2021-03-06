from rest_framework import serializers
from mmsapi.models import TopListComment

class TopListCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopListComment
        fields = ("toplist_id", 'user_id', 'text')
