from django.db import models


class InventoryItem(models.Model):
    property_name = models.CharField(max_length=30)
    category_name = models.CharField(max_length=30)
    unit_id = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=100)
    costing = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    is_inactive = models.CharField(max_length=30)

    def __str__(self):
        return self.property_name

