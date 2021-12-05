from django.db import models


class Charges(models.Model):
    charge_type_choices = [
        ('Rent', 'Rent'),
        ('Garbage', 'Garbage'),
        ('Internet', 'Internet'),
        ('Damages', 'Damages'),
        ('Deposit', 'Deposit'),
    ]
    payment_type_choices = [
        ('Cash', 'Cash'),
        ('Credit_Card', 'Credit_Card'),
        ('Bank', 'Bank'),
        ('Mpesa', 'Mpesa'),
    ]
    user_name = models.ForeignKey('tenant.Tenant', on_delete=models.CASCADE,)
    unit = models.CharField(max_length=30)
    charge_type = models.CharField(max_length=20, choices=charge_type_choices,)
    posted_by = models.CharField(max_length=30)
    description = models.CharField(max_length=20, choices=payment_type_choices,)
    amount = models.CharField(max_length=30)









