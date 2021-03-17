from rest_framework import viewsets
from mmsapi.models import ToWatch, Media
from mmsapi.serializers import ToWatchSerializer, ToWatchPostSerializer

class ToWatchViewSet(viewsets.ModelViewSet):
    queryset = ToWatch.objects.all()
    
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == "retrieve":
            return ToWatchSerializer
        if self.action == 'create':
            return ToWatchPostSerializer
        return ToWatchSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        searchstring = self.request.query_params.get('search', None)
        media_string = self.request.query_params.get('media', None)
        if user_id :
            userToWatch = ToWatch.objects.filter(user_id=user_id)
            allmedia = Media.objects.all()
            if media_string:
                searchqueryset = allmedia.filter(id__in=userToWatch.values('media_id')).filter(media_type=media_string)
            else:
                searchqueryset = allmedia.filter(id__in=userToWatch.values('media_id'))
            if searchstring:
                for term in searchstring:
                    searchqueryset = searchqueryset.filter(title__contains=term)  
            
            allToWatch = ToWatch.objects.all()
            filteredToWatch = allToWatch.filter(media_id__in= searchqueryset.values('id')).order_by("date_added")
            return filteredToWatch

        if user_id:
            self.queryset = ToWatch.objects.filter(user_id=user_id).order_by("date_added")
            return self.queryset
        else:
            return self.queryset