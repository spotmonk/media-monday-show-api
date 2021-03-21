from rest_framework import viewsets
from mmsapi.models import TopListItem
from mmsapi.serializers import TopListItemSerializer

class TopListItemViewSet(viewsets.ModelViewSet):
    queryset = TopListItem.objects.all()
    serializer_class = TopListItemSerializer

    