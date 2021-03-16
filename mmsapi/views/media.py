from rest_framework import viewsets
from mmsapi.models import Media, Episode
from mmsapi.serializers import MediaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from api_keys import tmdb_key
from tmdbv3api import TMDb, Movie, TV, Discover
from datetime import datetime, timedelta
from rest_framework import status



class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    def query_api(self, name):
        tmdb = TMDb()
        tmdb.api_key = tmdb_key
        tmdb.language = 'en'

        #search movies
        movie = Movie()
        search_movie = movie.search(name)
        
        for res in search_movie:
            try:
                Media.objects.get(external_id=res.id)
                continue
            except Media.DoesNotExist as ex:
                if res.release_date == '':
                    res.release_date = None
                if res.poster_path == None:
                    poster = "https://lascrucesfilmfest.com/wp-content/uploads/2018/01/no-poster-available-737x1024.jpg"
                else:
                    poster = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2" + res.poster_path
                Media.objects.create(
                    title = res.title,
                    description = res.overview,
                    poster_url = poster,
                    release_date = res.release_date,
                    media_type= "Movie",
                    external_id= res.id
                )


        #search TV
        tv = TV()
        search_tv = tv.search(name)

        for res in search_tv:
            if res.first_air_date == '':
                    res.first_air_date = None
            if res.poster_path == None:
                poster = "https://lascrucesfilmfest.com/wp-content/uploads/2018/01/no-poster-available-737x1024.jpg"
            else:
                poster = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2" + res.poster_path
            try:
                Media.objects.get(external_id=res.id)
                continue
            except Media.DoesNotExist as ex:
                Media.objects.create(
                    title = res.name,
                    description = res.overview,
                    poster_url = poster,
                    release_date = res.first_air_date,
                    media_type= "TV",
                    external_id= res.id
                )

    def discoverMedia(self, start_date, end_date):
        sd_str = datetime.strftime(start_date, '%Y-%m-%d')
        ed_str = datetime.strftime(end_date, '%Y-%m-%d')
        tmdb = TMDb()
        tmdb.api_key = tmdb_key
        tmdb.language = 'en'

        discover = Discover()
        movies = discover.discover_movies({
            'primary_release_date.gte': sd_str,
            'primary_release_date.lte': ed_str
        })

        for res in movies:
            try:
                Media.objects.get(external_id=res.id)
                continue
            except Media.DoesNotExist as ex:
                if res.release_date == '':
                    res.release_date = None
                if res.poster_path == None:
                    poster = "https://lascrucesfilmfest.com/wp-content/uploads/2018/01/no-poster-available-737x1024.jpg"
                else:
                    poster = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2" + res.poster_path
                Media.objects.create(
                    title = res.title,
                    description = res.overview,
                    poster_url = poster,
                    release_date = res.release_date,
                    media_type= "Movie",
                    external_id= res.id
                )

        
        series = discover.discover_tv_shows({
            'first_air_date.gte': sd_str,
            'first_air_date.lte': ed_str
        })

        for res in series:
            if res.first_air_date == '':
                    res.first_air_date = None
            if res.poster_path == None:
                poster = "https://lascrucesfilmfest.com/wp-content/uploads/2018/01/no-poster-available-737x1024.jpg"
            else:
                poster = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2" + res.poster_path
            try:
                Media.objects.get(external_id=res.id)
                continue
            except Media.DoesNotExist as ex:
                Media.objects.create(
                    title = res.name,
                    description = res.overview,
                    poster_url = poster,
                    release_date = res.first_air_date,
                    media_type= "TV",
                    external_id= res.id
                )

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        more = self.request.query_params.get('more', None)
        if name and more:
            #search api for name
            self.query_api(name=name)
            searchterm_list = name.split(' ')
            searchqueryset = Media.objects.all()
            for term in searchterm_list:
                searchqueryset = searchqueryset.filter(title__contains=term)
            return searchqueryset

        elif name:
            print(name)
            searchterm_list = name.split(' ')
            searchqueryset = Media.objects.all()
            for term in searchterm_list:
                searchqueryset = searchqueryset.filter(title__contains=term)
            return searchqueryset
        else:
            queryset = Media.objects.none()
            return self.queryset
    

    @action(methods=['get'], detail=False)
    def window(self, request):
        days = self.request.query_params.get('range', 14)
        daterange = timedelta(days=days)
        start_date = self.request.query_params.get('start_date', datetime.now())
        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.discoverMedia(start_date, start_date + daterange)
        media = Media.objects.all().order_by('release_date')
        mediawindow = media.filter(release_date__range=(start_date, start_date + daterange))
        serializer = MediaSerializer(mediawindow, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=['get'], detail=False, permission_classes=[] )
    def latest(self, request):
        episode = Episode.objects.latest('id')
        daterange = timedelta(days=14)
        media = Media.objects.all().order_by('release_date')
        mediawindow = media.filter(release_date__range=(episode.start_date, episode.start_date + daterange))
        if not mediawindow:
             self.discoverMedia(episode.start_date, episode.start_date + daterange)
             media = Media.objects.all()
             mediawindow = media.filter(release_date__range=(episode.start_date, episode.start_date + daterange))
        serializer = MediaSerializer(mediawindow, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
