from django.contrib.auth.models import AbstractUser, UserManager
from django.core import validators
from django.db import models


from utils.validators import validate_phone_number


class UserRole:
    """
    Роли пользователей
    """
    CUSTOMER = 'customer'  # Покупатель
    STAFF = 'staff'  # Сотрудник

    ROLE_CHOICES = (
        (CUSTOMER, 'Покупатель'),
        (STAFF, 'Сотрудник')
    )


class User(AbstractUser):
    """
    Модель пользователя
    """
    EMAIL_FIELD = 'username'

    username = models.CharField(
        'Адрес электронной почты',
        max_length=150,
        unique=True,
        help_text='Обязательное поле. Только буквы, цифры и следующие символы: @/./+/-/_.',
        validators=[validators.validate_email],
        error_messages={
            'unique': "Пользователь с таким адресом электронной почты уже существует.",
        },
    )
    first_name = models.CharField('Имя', max_length=30, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True, null=True)
    role = models.CharField('Роль', choices=UserRole.ROLE_CHOICES, max_length=20,
                            default=UserRole.CUSTOMER, db_index=True)
    phone = models.CharField('Номер телефона', max_length=20, validators=[validate_phone_number],
                             blank=True, null=True)
    objects = UserManager()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

