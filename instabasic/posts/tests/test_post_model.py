from django.test import TestCase
from users.models import CustomUser

from posts.models import Post
from .image import test_image

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
        self.assertTrue(self.post.image.name.startswith('posts/test_image'))
        self.assertEqual(self.post.description, 'Test Image!')
        posts = Post.objects.all()
        self.assertEqual(len(posts), 1)
        self.assertEqual(
            str(self.post),
            f'Post {self.post.image.name} by {self.author.username}'
        )
