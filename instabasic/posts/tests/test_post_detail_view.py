from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser
from posts.models import Post
from .image import test_image


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