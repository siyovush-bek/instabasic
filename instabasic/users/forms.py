from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)
    

class CustomUserUpdateForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'image')