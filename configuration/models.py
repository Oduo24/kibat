from django.db import models

# Create your models here.


class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    company_logo = models.CharField(max_length=30)



