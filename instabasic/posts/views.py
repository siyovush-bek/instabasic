from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView, 
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    paginate_by = 16


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'description']
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = '/posts/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
