from users.models import CustomUser
from uuid import uuid4
from django.db import models


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False, upload_to='posts')
    description = models.CharField(max_length=250, blank=True, default='')

    def __str__(self):
        return f'Post {self.image.name} by {self.author.username}'