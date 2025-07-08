from django.contrib.auth.models import User
from django.db import models

from clubs.models import Club


# Create your models here.
class Event(models.Model):
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name='events',
    )

    title = models.CharField(
        max_length=100,
    )

    date = models.DateField()

    location = models.CharField(
        max_length=255,
    )

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_events',
    )

    def __str__(self):
        return f'{self.title} ({self.club.name})'