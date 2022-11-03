from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    """
    Форма аутентификации
    """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CustomUserCreationForm(UserCreationForm):
    """
    Форма создания юзера
    """
    first_name = forms.CharField(max_length=30, required=True, label='Имя')
    last_name = forms.CharField(max_length=30, required=True, label='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

