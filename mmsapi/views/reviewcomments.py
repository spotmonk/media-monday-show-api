from rest_framework import viewsets
from mmsapi.models import ReviewComment
from mmsapi.serializers import ReviewCommentSerializer

class ReviewCommentViewSet(viewsets.ModelViewSet):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer


    def get_queryset(self):
        review_id = self.request.query_params.get('review_id', None)
        if review_id:
            self.queryset = ReviewComment.objects.filter(review_id=review_id)
            return self.queryset
        else:
            return self.queryset