from django.db import models
from product.models import Product

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    products = models.ManyToManyField(Product, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
