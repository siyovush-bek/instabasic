from django import forms
from django.forms import fields

from .models import Post


class CreatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('image', 'description',)
