from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse, resolve

from users.forms import CustomUserCreationForm

SIGNUP_URL = reverse('signup')


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