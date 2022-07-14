from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
