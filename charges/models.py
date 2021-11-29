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
    transaction_date = models.DateField
    charge_type = models.CharField(max_length=20, choices=charge_type_choices,)
    posted_by = models.CharField(max_length=30)
    Customer = models.ForeignKey('tenant.Tenant', on_delete=models.CASCADE,)
    Description = models. CharField(max_length=20, choices=payment_type_choices,)
    amount = models.CharField(max_length=30)







