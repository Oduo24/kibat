from django.db import models


class Tenant(models.Model):
    user_name = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=100)
    unit_id = models.ForeignKey('inventory.InventoryItem', on_delete=models.CASCADE)



