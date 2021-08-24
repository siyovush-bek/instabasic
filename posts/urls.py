from django.urls import path

from .views import post_list, post_detail, post_create

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<uuid:pk>', post_detail, name='post_detail'),
    path('create', post_create, 'post_create'),
]