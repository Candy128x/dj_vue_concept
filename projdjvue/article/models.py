from django.db import models

# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=250)
    body = models.TextField()