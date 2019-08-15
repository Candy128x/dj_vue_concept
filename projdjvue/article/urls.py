from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    # Web
    path('article_list/', TemplateView.as_view(template_name='index.html')),
]