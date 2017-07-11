from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """
    Custom User Class
    """
    username = models.CharField('username', max_length=12,
                                unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    class Meta():
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username
