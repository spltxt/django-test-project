from django.db import models
from django.contrib.auth import get_user_model

from utils.validators import validate_phone_number

User = get_user_model()


class Profile(models.Model):
    """
    Модель Профиль
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField('Номер телефона', max_length=20, validators=[validate_phone_number],
                             blank=True, null=True)

    def __str__(self):
        return f"Профиль {self.user.username}"

