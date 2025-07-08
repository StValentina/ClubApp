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


class Post(models.Model):
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    title = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_posts',
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_comments',
    )

    text = models.TextField()

    created_on = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Comment by {self.author.username}'