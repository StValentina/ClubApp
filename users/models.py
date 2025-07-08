from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        blank=True,
    )

    avatar_url = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'Profile {self.user.username}'