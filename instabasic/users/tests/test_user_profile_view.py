from django.urls.base import reverse
from users.models import CustomUser
from django.test import TestCase


class TestUserProfileView(TestCase):
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
    
    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
        self.assertContains(response, self.user.username)

    def tearDown(self):
        self.client.logout()