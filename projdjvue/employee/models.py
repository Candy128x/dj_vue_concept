from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class EmpInfo(models.Model):
    first_name  = models.CharField(max_length=128)
    last_name   = models.CharField(max_length=128)
    username    = models.CharField(max_length=128)
    age         = models.IntegerField(default=0,
                    validators=[MinValueValidator(0), MaxValueValidator(128)])
    dob         = models.DateField()
    address     = models.TextField()
    email_id    = models.EmailField()
    contact_no  = models.CharField(max_length=12)
    extra       = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username'], name='username_unique'),
            # models.UniqueConstraint(fields=['email_id'], name='email_id_unique')
        ]


class CompanyList(models.Model):
    name        = models.CharField(max_length=256)
    emp         = models.ForeignKey(EmpInfo, on_delete=models.CASCADE)
    salary      = models.BigIntegerField()
    date_of_join = models.DateField()
    experience  = models.IntegerField()
