"""mms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mmsapi.views import *
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'episodecomments', EpisodeCommentViewSet, 'episodecomment')
router.register(r'episodes', EpisodeViewSet, 'episode')
router.register(r'hostrecommendations', HostRecommendationViewSet, 'hostrecommendation')
router.register(r'media', MediaViewSet, 'media')
router.register(r'rankings', RankingViewSet, 'ranking')
router.register(r'recommendations', RecommendationViewSet, 'recommendation')
router.register(r'recommendationvotes', RecommendationVoteViewSet, 'recommendationvote')
router.register(r'reviewcomments', ReviewCommentViewSet, 'reviewcomment')
router.register(r'reviews', ReviewsViewSet, 'review')
router.register(r'toplists', ToplistViewSet, 'toplist')
router.register(r'toplistcomments', TopListCommentViewSet, 'toplistcomment')
router.register(r'toplistitems', TopListItemViewSet, 'toplistitems')
router.register(r'towatch', ToWatchViewSet, 'towatch')
router.register(r'watched', WatchedViewSet, 'watched')
router.register(r'images', ImageViewSet, 'image')




urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
