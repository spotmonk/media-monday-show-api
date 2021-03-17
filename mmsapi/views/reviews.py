from rest_framework import viewsets
from mmsapi.models import Review
from mmsapi.serializers import ReviewSerializer, ReviewPostSerializer
from rest_framework.response import Response
from rest_framework import status

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        media_id = self.request.query_params.get('media_id', None)
        if media_id:
            self.queryset = Review.objects.filter(media_id=media_id)
            return self.queryset
        else:
            return self.queryset
    
    def create(self, request):
        serializer = ReviewPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)