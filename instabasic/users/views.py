from django.contrib.auth.models import User
from django.http import request
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import UpdateView

from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser
from posts.models import Post

@login_required
def profile(request, pk=None):
    if pk is None:
        pk = request.user.id
    user = get_object_or_404(CustomUser, id=pk)
    posts = Post.objects.filter(author=user)
    return render(request, 'users/profile.html', {'user':user, 'posts':posts})


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    fields = ('username', 'email', 'image',)
    template_name = 'users/update.html'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
