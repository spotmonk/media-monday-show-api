from rest_framework import viewsets
from mmsapi.models import Toplist
from mmsapi.serializers import ToplistSerializer

class ToplistViewSet(viewsets.ModelViewSet):
    queryset = Toplist.objects.all()
    serializer_class = ToplistSerializer
