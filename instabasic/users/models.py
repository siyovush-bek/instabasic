from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('profile', args=[self.id])
