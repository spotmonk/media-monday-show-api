from rest_framework import viewsets
from mmsapi.models import ToWatch
from mmsapi.serializers import ToWatchSerializer

class ToWatchViewSet(viewsets.ModelViewSet):
    queryset = ToWatch.objects.all()
    serializer_class = ToWatchSerializer
