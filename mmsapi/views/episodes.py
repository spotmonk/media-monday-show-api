from rest_framework import viewsets
from mmsapi.models import Episode
from mmsapi.serializers import EpisodeSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
