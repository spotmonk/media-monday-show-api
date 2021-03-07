from rest_framework import viewsets
from mmsapi.models import Review
from mmsapi.serializers import ReviewSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
