from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Song
from .serializers import MovieSerializer, SongSerializer

# Create your views here.


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
