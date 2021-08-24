from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Post
from users.models import CustomUser

test_image = SimpleUploadedFile(
    'test_image.jpg', 
    content= open('test_jpg.jpg', 'rb').read(), 
    content_type='image/jpeg'
)


class PostModelTest(TestCase):
    def setUp(self):
        self.author = CustomUser.objects.create_user(
            username='test_user', email='test@dot.com',
            password='123test'
        )
        self.post = Post(
            image=test_image,
            author=self.author,
            description='Test Image!'
        )
        self.post.save()
    
    def test_fields(self):
        self.assertEqual(self.post.author, self.author)
        self.assertEqual(self.post.description, 'Test Image!')
        posts = Post.objects.all()
        self.assertEqual(len(posts), 1)
        self.assertEqual(
            str(self.post),
            f'Post {self.post.image.name} by {self.author.username}'
        )

    # def test_post_empty_fields(self):
    #     post_empty_fields = Post()
    #     post_empty_fields.save()
    #     posts = Post.objects.all()
    #     self.assertEqual(len(posts), 1)
