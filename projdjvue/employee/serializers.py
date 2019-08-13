from rest_framework import serializers
from .models import EmpInfo, CompanyList


class EmpInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpInfo
        fields = ('__all__')


class CompListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyList
        fields = ('__all__')