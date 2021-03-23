from rest_framework import viewsets
from mmsapi.models import Ranking, MMSUser
from mmsapi.serializers import RankingSerializer, RankingReadSerializer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == "retrieve":
            return RankingReadserializer
        return RankingSerializer


    def list(self, request):
        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        all_rankings = Ranking.objects.all()
        filtered_ranking = all_rankings.filter(ranking__isnull=False)
        rankings = filtered_ranking.filter(user_id=mmsuser).order_by('ranking')
        serializer = RankingReadSerializer(rankings, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def update(self, request, pk):
        ranking = self.get_object()
        serializer = RankingSerializer(ranking, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HttpResponseBadRequest.status_code)

    def destroy(self, request):
        instance = self.get_object()
        all_rankings = Ranking.objects.all()
        filtered_ranking = all_rankings.filter(ranking__isnull=False)
        rankings = filtered_ranking.filter(user_id=mmsuser)
        for ranking in rankings:
            if ranking.ranking > instance.ranking:
                ranking.ranking = ranking.ranking - 1


    @action(detail=False)
    def increase(self, request):
        id = request.query_params.get('id')
        instance = Ranking.objects.get(pk=id)
        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        all_rankings = Ranking.objects.all()
        rankings = all_rankings.filter(user_id=mmsuser)
        higher = rankings.get(ranking=instance.ranking - 1)
        instance.ranking = instance.ranking - 1
        instance.save()
        higher.ranking = higher.ranking + 1
        higher.save()
        return Response({"Increased"}, status=status.HTTP_200_OK)


    @action(detail=False)
    def decrease(self, request):
        id = request.query_params.get('id')
        instance = Ranking.objects.get(pk=id)
        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        all_rankings = Ranking.objects.all()
        rankings = all_rankings.filter(user_id=mmsuser)
        higher = rankings.get(ranking=instance.ranking + 1)
        instance.ranking = instance.ranking + 1
        instance.save()
        higher.ranking = higher.ranking - 1
        higher.save()
        return Response({"Decreased"}, status=status.HTTP_200_OK)

    
    @action(detail=False)
    def insert(self, request):
        id = request.query_params.get('id')
        new_ranking = request.query_params.get('ranking')
        instance = Ranking.objects.get(pk=id)
        instance.ranking = new_ranking
        instance.save()

        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        all_rankings = Ranking.objects.all()
        rankings = all_rankings.filter(user_id=mmsuser)
        ranking = rankings.filter(media_id=instance.media_id)
        ranked = rankings.filter(ranking__isnull=False)
        for rank in ranked:
            if rank.ranking >= int(new_ranking):
                rank.ranking = rank.ranking + 1
                rank.save()
        instance = Ranking.objects.get(pk=id)
        instance.ranking = new_ranking
        instance.save()
        return Response({"Inserted"}, status=status.HTTP_200_OK)

class UnrankedViewSet(viewsets.ModelViewSet):
    
    def list(self, request):
        mmsuser = MMSUser.objects.get(user_id=request.auth.user)
        all_rankings = Ranking.objects.all()
        filtered_ranking = all_rankings.filter(ranking__isnull=True)
        rankings = filtered_ranking.filter(user_id=mmsuser)
        serializer = RankingReadSerializer(rankings, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    