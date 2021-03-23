from rest_framework import viewsets
from mmsapi.models import Toplist, Ranking, MMSUser, TopListItem
from mmsapi.serializers import ToplistSerializer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class ToplistViewSet(viewsets.ModelViewSet):
    queryset = Toplist.objects.all()
    serializer_class = ToplistSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            self.queryset = Toplist.objects.filter(user_id=user_id)
            return self.queryset
        else:
            return self.queryset

    @action(detail=False)
    def new(self, request):
        title = request.query_params.get('title')
        number = request.query_params.get('number')
        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        all_rankings = Ranking.objects.all()
        rankings = all_rankings.filter(user_id=mmsuser)
        ranked = rankings.filter(ranking__isnull=False).filter(ranking__lte=number).order_by('ranking')
        top_list = Toplist()
        top_list.title = title
        top_list.user_id = mmsuser
        top_list.save()
        for item in ranked:
            list_item = TopListItem()
            list_item.user_id = mmsuser
            list_item.ranking = item.ranking
            list_item.media_id = item.media_id
            list_item.save()
            top_list.toplist_items.add(list_item)
        top_list.save()

        serializer = ToplistSerializer(top_list)
        return Response(serializer.data, status=status.HTTP_201_CREATED)