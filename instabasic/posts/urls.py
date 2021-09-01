from django.urls import path

from .views import PostDetailView, PostsListView, PostCreateView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('create/', PostCreateView.as_view(), name='posts_create'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('create/', post_create, name='post_create'),
]