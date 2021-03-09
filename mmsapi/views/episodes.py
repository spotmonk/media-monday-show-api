from rest_framework import viewsets
from mmsapi.models import Episode
from mmsapi.serializers import EpisodeSerializer
from bs4 import BeautifulSoup
import requests
from dateutil.parser import *
from datetime import datetime
from django.db import IntegrityError

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

    
        
    def parse_episodes(self):
        response = requests.get('https://anchor.fm/s/1037cfac/podcast/rss')
        soup = BeautifulSoup(response.content, 'xml')

        items = soup.find_all("item")
        descriptiondivs = []
        titledivs = []
        linksdivs = []
        pubdatedivs = []
        episodetypedivs = []
        for item in items:
            titledivs.append(item.title)
            descriptiondivs.append(item.find("itunes:summary"))
            linksdivs.append(item.find('link'))
            pubdatedivs.append(item.pubDate)
            episodetypedivs.append(item.find("itunes:episodeType"))
        i = len(descriptiondivs) - 1
        while i >= 0:
            splitlink = linksdivs[i].text.split('/')
            
            if episodetypedivs[i] is None:
                episodetype = "Full"
            else: 
                episodetype = episodetypedivs[i].text

            try:
                episode = Episode.objects.create(
                title = titledivs[i].text,
                blurb = descriptiondivs[i].text,
                host_comments = "",
                start_date = parse(pubdatedivs[i].text),
                episode_type = episodetype,
                url = splitlink[5]
                )
            except IntegrityError as e:
                    pass
            i = i - 1

    def list(self, request):
        self.parse_episodes()
        queryset = Episode.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)