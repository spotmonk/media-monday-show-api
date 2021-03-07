from rest_framework import viewsets
from mmsapi.models import Recommendation
from mmsapi.serializers import RecommendationSerializer

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
