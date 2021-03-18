from rest_framework import viewsets
from mmsapi.models import Watched, Media
from mmsapi.serializers import WatchedSerializer, WatchedPostSerializer

class WatchedViewSet(viewsets.ModelViewSet):
    queryset = Watched.objects.all()
    serializer_class = WatchedSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == "retrieve":
            return WatchedSerializer
        if self.action == 'create':
            return WatchedPostSerializer
        return WatchedSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        searchstring = self.request.query_params.get('search', None)
        media_string = self.request.query_params.get('media', None)
        if user_id :
            userWatched = Watched.objects.filter(user_id=user_id)
            allmedia = Media.objects.all()
            if media_string:
                searchqueryset = allmedia.filter(id__in=userWatched.values('media_id')).filter(media_type=media_string)
            else:
                searchqueryset = allmedia.filter(id__in=userWatched.values('media_id'))
            if searchstring:
                for term in searchstring:
                    searchqueryset = searchqueryset.filter(title__contains=term)  
            
            allWatched = Watched.objects.all()
            filteredWatched = allWatched.filter(media_id__in= searchqueryset.values('id')).order_by("date_watched")
            return filteredWatched

        if user_id:
            self.queryset = Watched.objects.filter(user_id=user_id).order_by("date_watched")
            return self.queryset
        else:
            return self.queryset