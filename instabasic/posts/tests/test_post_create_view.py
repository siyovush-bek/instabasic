from django.http import response
from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser
from posts.forms import CreatePostForm

class CreatePostView(TestCase):
    url = reverse('posts_create')
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='test_user',
            email='test@test.com',
            password='123password'
        )
        self.user.save()
        self.client.login(
            username=self.user.username,
            password='123password'
        )
        

    def test_not_logged_user_cannot_create_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
    
    def test_logged_users_create_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_create.html')
        # form = response.context.get('form')
        # self.assertIsInstance(form, CreatePostForm)
        self.assertContains(response, 'csrfmiddlewaretoken')
    
    def tearDown(self):
        self.client.logout()
