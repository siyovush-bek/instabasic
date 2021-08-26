from http import HTTPStatus
from django.contrib import messages
from django.test import TestCase
from django.urls import reverse, resolve

from .models import CustomUser
from .forms import CustomUserCreationForm

SIGNUP_URL = reverse('signup')


class CustomUserTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='test_user', email='test@dot.com',
            password='123test'
        )
    
    def test_user_credentials(self):
        self.assertEqual(self.user.username, 'test_user')
        self.assertEqual(self.user.email, 'test@dot.com')
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)
    
    def test_user__default_image(self):
        self.assertEqual(self.user.image, 'default.jpg')

class UserSignUpTest(TestCase):

    def setUp(self):
        self.response = self.client.get(SIGNUP_URL)
    
    def test_signup_page(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(self.response, 'users/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Welcome!')
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_sign_view(self):
        view = resolve('/signup/')
        self.assertEqual(
            view.func.__name__,
            'signup'
        )

class UserCreationTest(TestCase):
    def test_post_success(self):
        data = {
            'username': 'test_user',
            'email': 'test@email.com',
            'password1': '123passw',
            'password2': '123passw',
        }
        response = self.client.post(
            '/signup/', data=data
        )
        self.assertRedirects(response, reverse('login'))
