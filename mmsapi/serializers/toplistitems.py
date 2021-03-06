from rest_frammework import serializers
from mmsapi.models import TopListItem

class TopListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopListItem
        fields = ('toplist_id', 'user_id', 'ranking')
