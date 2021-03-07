from rest_framework import viewsets
from mmsapi.models import Media
from mmsapi.serializers import MediaSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
