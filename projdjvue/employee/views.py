from django.shortcuts import render
from django.db.models import Min, Max
from rest_framework import viewsets, filters
from .models import EmpInfo, CompanyList
from .serializers import EmpInfoSerializer, CompListSerializer

# Create your views here.


class EmpInfoView(viewsets.ModelViewSet):
    queryset = EmpInfo.objects.all()
    serializer_class = EmpInfoSerializer


class CompListView(viewsets.ModelViewSet):
    queryset = CompanyList.obects.all()
    serializer_class = CompListSerializer