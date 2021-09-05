from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.postgres.search import TrigramSimilarity
from django.views.generic import UpdateView, ListView

from .forms import CustomUserCreationForm
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


class SearchResultListView(ListView):
    model = CustomUser
    context_object_name = 'user_list'
    template_name = 'users/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = CustomUser.objects.annotate(
                similarity=TrigramSimilarity('username', query),
                ).filter(similarity__gt=0.1).order_by('-similarity')
        return results