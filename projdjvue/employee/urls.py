from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/employee', views.EmpInfoView)
# router.register('comp_list', views.CompListView)


urlpatterns = [
    path('', include(router.urls)),
]
