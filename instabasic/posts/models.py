from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(null=False, blank=False, upload_to='posts')
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250, blank=True, default='')

    def __str__(self):
        return f'Post {self.image.name} by {self.author.username}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id),])
