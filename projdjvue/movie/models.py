from django.db import models

# Create your models here.


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    lanuch_date = models.DateField()

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)