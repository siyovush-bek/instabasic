from django.http import response
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

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
        self.assertTrue(self.post.image.name.startswith('posts/test_image'))
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


class TestPostDetailView(TestCase):
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
    
    def test_lists_page(self):
        url = reverse('posts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/posts_list.html')
        self.assertContains(response, self.post.image.name)

    def test_detail_page(self):
        url = self.post.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_detail.html')
        self.assertContains(response, self.post.image.name)
        self.assertContains(response, self.post.description)

