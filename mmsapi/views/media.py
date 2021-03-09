from rest_framework import viewsets
from mmsapi.models import Media
from mmsapi.serializers import MediaSerializer
from api_keys import tmdb_key
from tmdbv3api import TMDb, Movie, TV


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

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        more = self.request.query_params.get('more', None)
        if name and more:
            #search api for name
            self.query_api(name=name)
            return self.queryset.filter(title__contains=name)

        elif name:
            return self.queryset.filter(title__contains=name)
        else:
            return self.queryset