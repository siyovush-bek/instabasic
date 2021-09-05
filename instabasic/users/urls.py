from django.urls import path
from .views import profile, signup, ProfileUpdateView, SearchResultListView
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('search/', SearchResultListView.as_view(), name='search_results'),
    path('users/<int:pk>/', profile, name='profile'),
    path('users/<int:pk>/update/', ProfileUpdateView.as_view(), name='update'),
]

