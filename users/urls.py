from django.urls import path
from .views import profile, signup
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
]

