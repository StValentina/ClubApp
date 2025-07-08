from django.contrib.auth.models import User
from django.db import models

from clubs.models import Club


# Create your models here.
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