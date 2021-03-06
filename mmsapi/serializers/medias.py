from rest_frammework import serializers
from mmsapi.models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('title', 'description', 'poster_url', 'release_date', 'media_type', 'external_id')
