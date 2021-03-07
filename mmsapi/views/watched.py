from rest_framework import viewsets
from mmsapi.models import Watched
from mmsapi.serializers import WatchedSerializer

class WatchedViewSet(viewsets.ModelViewSet):
    queryset = Watched.objects.all()
    serializer_class = WatchedSerializer
