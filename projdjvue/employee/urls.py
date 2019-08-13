from rest_framework import routers
from . import views
from django.urls import path, include
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'employee', views.EmpInfoView)
# router.register(r'comp_list', views.CompListView)


urlpatterns = [
    # API
    path('', include(router.urls)),

    # Web
    path('employee/', TemplateView.as_view(template_name='index.html')),
]