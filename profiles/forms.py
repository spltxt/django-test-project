from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    Форма профиля
    """
    class Meta:
        model = Profile
        exclude = ('user',)
