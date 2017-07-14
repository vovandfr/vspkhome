from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tweets(models.Model):
    """Tweet model"""
    user = models.ForeignKey(User)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    class Meta():
        verbose_name_plural = 'Tweets'

    def __str__(self):
        return self.text


class HashTag(models.Model):
    """HashTag model"""
    name = models.CharField(max_length=64, unique=True)
    tweet = models.ManyToManyField(Tweets)

    class Meta():
        verbose_name_plural = 'HashTags'

    def __str__(self):
        return self.name
