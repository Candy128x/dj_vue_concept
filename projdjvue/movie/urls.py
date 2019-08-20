from django.urls import path, include
from . import views
from rest_framework import routers
# from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register('api/movie', views.MovieView)
router.register('api/song', views.SongView)


urlpatterns = [
    # API
    path('', include(router.urls)),

    # Web
    # path('article_list/', TemplateView.as_view(template_name='index.html')),
    path('movie_index', views.index, name='index')
]