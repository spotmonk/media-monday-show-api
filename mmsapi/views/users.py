from rest_framework import viewsets
from mmsapi.models import MMSUser, ToWatch, Watched
from mmsapi.serializers import MMSUserSerializer, ToWatchSerializer, WatchedSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = MMSUser.objects.all()
    serializer_class = MMSUserSerializer


    @action(methods=['get'], detail=False )
    def current(self, request):
        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        serializer = MMSUserSerializer(mmsuser, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=['get'], detail=False )
    def watchlist(self, request):
        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        towatch = ToWatch.objects.filter(user_id=mmsuser)
        watched = Watched.objects.filter(user_id=mmsuser)
        towatchserialized = ToWatchSerializer(towatch, many=True)
        watchedserialized = WatchedSerializer(watched, many=True)
        serializer = MMSUserSerializer(mmsuser, context={'request': request})
        return Response({"user": serializer.data, "toWatch": towatchserialized.data, "watched": watchedserialized.data}, status=status.HTTP_200_OK)