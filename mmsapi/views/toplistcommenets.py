from rest_framework import viewsets
from mmsapi.models import TopListComment
from mmsapi.serializers import TopListCommentSerializer

class TopListCommentViewSet(viewsets.ModelViewSet):
    queryset = TopListComment.objects.all()
    serializer_class = TopListCommentSerializer
