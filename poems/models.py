from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ACCOUNT_TYPES = [
        ('free', 'Free'),
        ('pro', 'Pro'),
        ('premium', 'Premium'),
    ]
    account_type = models.CharField(
        max_length=10,
        choices=ACCOUNT_TYPES,
        default='free'
    )

class CustomUser(AbstractUser):
    theme = models.CharField(max_length=20, default="light")

class Poem(models.Model):
    title = models.CharField(max_length=255, default="Без назви")
    text = models.TextField()
    image = models.ImageField(upload_to='poems_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=250,
    )
    text = models.CharField(
        max_length=10000,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )


    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.CharField(max_length=10000)
    poem = models.ManyToManyField(
        "Poem",
        related_name="review",
        null=True
    )
    author_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.text[:10]
