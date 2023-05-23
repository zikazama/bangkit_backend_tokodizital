from django.db import models

def upload_to(instance, filename):
    return 'product/images/{filename}'.format(filename=filename)

# create product model
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=200, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

