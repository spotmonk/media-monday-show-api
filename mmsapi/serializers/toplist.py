from rest_framework import serializers
from mmsapi.models import Toplist
from .toplistitems import TopListItemSerializer

class ToplistSerializer(serializers.ModelSerializer):
    toplist_items = TopListItemSerializer(read_only=True, many=True)
    class Meta:
        model = Toplist
        fields = ('id','title', 'date', 'user_id', 'toplist_items')
