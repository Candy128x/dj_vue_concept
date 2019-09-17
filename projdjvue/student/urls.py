from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from student import views

urlpatterns = [
    path('list/', views.StudentDetailsList.as_view()),
    path('detail/<int:pk>/', views.StudentDetailsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)