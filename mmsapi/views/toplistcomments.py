from rest_framework import viewsets
from mmsapi.models import TopListComment
from mmsapi.serializers import TopListCommentSerializer, TopListCommentPostSerializer

class TopListCommentViewSet(viewsets.ModelViewSet):
    queryset = TopListComment.objects.all()
    serializer_class = TopListCommentSerializer

    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == "retrieve":
            return TopListCommentSerializer
        if self.action == 'create':
            return TopListCommentPostSerializer
        return TopListCommentSerializer


    def get_queryset(self):
        toplist_id = self.request.query_params.get('toplist_id', None)
        if toplist_id:
            return self.queryset.filter(toplist_id=toplist_id)
        else:
            return self.queryset