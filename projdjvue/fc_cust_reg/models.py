from django.db import models
from fc_common.models import Documents
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class CompanyDetails(models.Model):
    annual_logistic_spend_currency = models.CharField(max_length=255)
    annual_logistic_spend = models.BigIntegerField()
    annual_air_shipments = models.IntegerField()
    annual_lcl_shipments = models.IntegerField()
    annual_fcl_shipments = models.IntegerField()
    total_shipments = models.IntegerField()
    annual_air_volume = models.IntegerField()
    annual_lcl_volume = models.IntegerField()
    annual_fcl_volume = models.IntegerField()
    incorporation_year = models.IntegerField()
    incorporation_number = models.IntegerField()
    annual_revenue_currency = models.CharField(max_length=5)
    annual_revenue = models.BigIntegerField()


class Company(models.Model):
    name = models.CharField(max_length=255)
    company_type = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    business_activity = models.CharField(max_length=255)
    iec = models.CharField(max_length=30)
    gst = models.CharField(max_length=30)
    pan = models.CharField(max_length=30)
    cin = models.CharField(max_length=30)
    logo = models.ForeignKey(Documents, on_delete=models.CASCADE)
    company_bio = models.TextField()
    company_structure = models.CharField(max_length=255)
    company_details = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)


class Addresses(models.Model):
    entity_type = models.CharField(max_length=255)
    entity_id = models.IntegerField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class CompanyCountries(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_country_id = models.ForeignKey(Addresses, on_delete=models.CASCADE)
