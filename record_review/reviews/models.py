from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Review(models.Model):
    artist = models.CharField(max_length=100, verbose_name='Band or Artist Name')
    album = models.CharField(max_length=200, verbose_name='Album Name')
    rating = models.FloatField()
    content = models.TextField(verbose_name='Your Album Review')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Add Album Image', default='default.jpg', upload_to='album_pics')

    def __str__(self):
        return '%s - %s' % (self.artist, self.album)

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})