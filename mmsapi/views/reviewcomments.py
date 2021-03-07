from rest_framework import viewsets
from mmsapi.models import ReviewComment
from mmsapi.serializers import ReviewCommentSerializer

class ReviewCommentViewSet(viewsets.ModelViewSet):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
