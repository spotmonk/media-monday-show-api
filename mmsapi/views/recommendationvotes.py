from rest_framework import viewsets
from mmsapi.models import RecommendationVote
from mmsapi.serializers import RecommendationVoteSerializer

class RecommendationVoteViewSet(viewsets.ModelViewSet):
    queryset = RecommendationVote.objects.all()
    serializer_class = RecommendationVoteSerializer
