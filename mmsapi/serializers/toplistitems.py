from rest_framework import serializers
from mmsapi.models import TopListItem

class TopListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopListItem
        fields = ('toplist_id', 'user_id', 'ranking')
