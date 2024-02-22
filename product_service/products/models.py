import uuid

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=224, null=False, blank=False)
    price = models.DecimalField(max_digits=10000000000, decimal_places=2, null=False, blank=False)
    description = models.TextField()
    quantity = models.IntegerField()
    sold_quantity = models.IntegerField()
