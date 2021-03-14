from rest_framework import serializers
from mmsapi.models import MMSUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class MMSUserSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    class Meta:
        model = MMSUser
        fields = ('id', 'bio', 'profile_image_url', 'user_id')
