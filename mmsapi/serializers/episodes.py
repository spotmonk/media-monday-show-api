from rest_framework import serializers
from mmsapi.models import Episode

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('title', 'blurb', 'host_comments', 'start_date', 'url', 'episode_type')
