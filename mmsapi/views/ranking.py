from rest_framework import viewsets
from mmsapi.models import Ranking
from mmsapi.serializers import RankingSerializer

class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
