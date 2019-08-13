from rest_framework import routers
from . import views
from django.urls import path, include
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'article', views.ArticleView)


urlpatterns = [
    # API
    path('', include(router.urls)),

    # Web
    path('article_list/', TemplateView.as_view(template_name='index.html')),
]