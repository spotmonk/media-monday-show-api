from rest_framework import viewsets
from mmsapi.models import EpisodeComment
from mmsapi.serializers import EpisodeCommentSerializer, EpisodeCommentPostSerializer

class EpisodeCommentViewSet(viewsets.ModelViewSet):
    queryset = EpisodeComment.objects.all()
    serializer_class = EpisodeCommentSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == "retrieve":
            return EpisodeCommentSerializer
        if self.action == 'create':
            return EpisodeCommentPostSerializer
        return EpisodeCommentSerializer


    def get_queryset(self):
        episode_id = self.request.query_params.get('episode_id', None)
        if episode_id:
            return self.queryset.filter(episode_id=episode_id)
        else:
            return self.queryset
