from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # The same many2one relationship in odoo
    # (user in table Profile n-1 user in table User in database)
    # on_delete=models.CASCADE: when user in table User delete
    #   -> Profile related this user will be deleted too.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...")
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
