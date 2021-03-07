from rest_framework import viewsets
from mmsapi.models import EpisodeComment
from mmsapi.serializers import EpisodeCommentSerializer

class EpisodeCommentViewSet(viewsets.ModelViewSet):
    queryset = EpisodeComment.objects.all()
    serializer_class = EpisodeCommentSerializer
