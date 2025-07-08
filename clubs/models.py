from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    category = models.CharField(
        max_length=100,
    )

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_clubs',
    )

    def __str__(self):
        return self.name