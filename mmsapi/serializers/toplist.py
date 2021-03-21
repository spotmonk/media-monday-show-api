from rest_framework import serializers
from mmsapi.models import Toplist, MMSUser
from .toplistitems import TopListItemSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class MMSUserSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    class Meta:
        model = MMSUser
        fields = ( 'user_id', )

class ToplistSerializer(serializers.ModelSerializer):
    toplist_items = TopListItemSerializer(read_only=True, many=True)
    user_id = MMSUserSerializer(read_only=True)
    class Meta:
        model = Toplist
        fields = ('id','title', 'date', 'user_id', 'toplist_items')
