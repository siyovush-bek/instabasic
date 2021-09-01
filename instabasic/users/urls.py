from django.urls import path
from .views import profile, signup, ProfileUpdateView
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('users/<int:pk>/', profile, name='profile'),
    path('users/<int:pk>/update/', ProfileUpdateView.as_view(), name='update'),
]

