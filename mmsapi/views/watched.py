from rest_framework import viewsets
from mmsapi.models import Watched, Media, Ranking, MMSUser
from mmsapi.serializers import WatchedSerializer, WatchedPostSerializer
from rest_framework.response import Response
from rest_framework import status

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

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        all_rankings = Ranking.objects.all()
        rankings = all_rankings.filter(user_id=mmsuser)
        ranking = rankings.filter(media_id=instance.media_id)
        ranked = rankings.filter(ranking__isnull=False)
        for rank in ranked:
            if rank.ranking > ranking[0].ranking:
                rank.ranking = rank.ranking - 1
                rank.save()

        self.perform_destroy(ranking)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
        