from rest_framework import viewsets
from mmsapi.models import EpisodeComment
from mmsapi.serializers import EpisodeCommentSerializer

class EpisodeCommentViewSet(viewsets.ModelViewSet):
    queryset = EpisodeComment.objects.all()
    serializer_class = EpisodeCommentSerializer


    def get_queryset(self):
        episode_id = self.request.query_params.get('episode_id', None)
        if episode_id:
            return self.queryset.filter(episode_id=episode_id)
        else:
            return self.queryset
