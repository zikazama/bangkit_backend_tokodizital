from django.db import models
from authentication.models import AuthUser
from disease.models import Disease

def upload_to(instance, filename):
    print(instance)
    return 'history/images/{instance.user.id}/{instance.timestamp}/{filename}'.format(instance=instance, filename=filename)

class History(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to=upload_to)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)