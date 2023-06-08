from django.db import models

from authentication.models.users import AuthUser
from blog.models import Blog

class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog_id)