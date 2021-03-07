from rest_framework import viewsets
from mmsapi.models import HostRecommendation
from mmsapi.serializers import HostRecommendationSerializer

class HostRecommendationViewSet(viewsets.ModelViewSet):
    queryset = HostRecommendation.objects.all()
    serializer_class = HostRecommendationSerializer
