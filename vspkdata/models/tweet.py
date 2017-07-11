from django.db import models
from vspkdata.models import User


class Tweet(models.Model):
    """
    Tweet model
    """
    user = models.ForeignKey(User)
    text = models.CharField(max_length=160)
    create_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.text
