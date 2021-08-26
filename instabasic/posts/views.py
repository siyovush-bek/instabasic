from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
