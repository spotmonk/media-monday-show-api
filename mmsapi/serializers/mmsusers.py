from rest_framework import serializers
from mmsapi.models import MMSUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class MMSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MMSUser
        fields = ('id', 'bio', 'profile_image_url', 'created_on', 'active', 'user_id')
