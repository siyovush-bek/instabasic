from django.test import TestCase

from users.models import CustomUser



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

