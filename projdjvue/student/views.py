from django.shortcuts import render
from student.models import StudentDetails
from student.serializers import StudentDetailsSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


class StudentDetailsList(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):

    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetailsDetail(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):

    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
