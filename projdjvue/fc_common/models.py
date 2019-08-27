from django.db import models

# Create your models here.


class Documents(models.Model):
    entity_type = models.CharField(max_length=255)
    entity_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)