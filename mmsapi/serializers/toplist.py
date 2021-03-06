from rest_frammework import serializers
from mmsapi.models import Toplist

class ToplistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toplist
        fields = ('title', 'date', 'user_id')
