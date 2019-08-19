from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register('api/article', views.ArticleView)


urlpatterns = [
    # API
    path('', include(router.urls)),

    # Web
    path('article_list/', TemplateView.as_view(template_name='index.html')),
]