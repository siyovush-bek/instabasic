from django.urls import path

from .views import (
    PostDeleteView, 
    PostDetailView, 
    PostsListView, 
    PostCreateView, 
    PostUpdateView,
)

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('create/', PostCreateView.as_view(), name='posts_create'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<uuid:pk>/update/', PostUpdateView.as_view(), name='post_update'),
]