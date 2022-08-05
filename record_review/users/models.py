from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=100)
    favorite_artists = models.TextField(max_length=200)
    about_user = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'