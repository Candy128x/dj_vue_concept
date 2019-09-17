from django.db import models

# Create your models here.


class StudentDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=16)
