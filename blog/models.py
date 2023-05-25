from django.db import models
from datetime import datetime
from authentication.models import AuthUser

def upload_to(instance, filename):
    return 'blog/images/{instance.user.id}/{time}/{filename}'.format(instance=instance, filename=filename, time=datetime.now())

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_to)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AuthUser,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
