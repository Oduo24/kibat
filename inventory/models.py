from django.db import models


class InventoryItem(models.Model):
    property_name = models.CharField(max_length=30)

    BEDSITTER = 'BS'
    ONEBEDROOM = '1B'
    TWOBEDROOM = '2B'
    OFFICESPACE = 'OS'
    CATEGORY_NAME_CHOICES = [
        (BEDSITTER, 'Bedsitter'),
        (ONEBEDROOM, '1-Bedroom'),
        (TWOBEDROOM, '2-Bedroom'),
        (OFFICESPACE, 'Office'),
    ]
    category_name = models.CharField(max_length=2, choices=CATEGORY_NAME_CHOICES, default=BEDSITTER)
    unit_id = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=100)
    costing = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    is_inactive = models.CharField(max_length=30)

    def __str__(self):
        return self.property_name


















