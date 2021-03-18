from rest_framework import viewsets
from mmsapi.models import ReviewComment
from mmsapi.serializers import ReviewCommentSerializer, ReviewCommentPostSerializer

class ReviewCommentViewSet(viewsets.ModelViewSet):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == "retrieve":
            return ReviewCommentSerializer
        if self.action == 'create':
            return ReviewCommentPostSerializer
        return ReviewCommentSerializer


    def get_queryset(self):
        review_id = self.request.query_params.get('review_id', None)
        if review_id:
            self.queryset = ReviewComment.objects.filter(review_id=review_id)
            return self.queryset
        else:
            return self.queryset