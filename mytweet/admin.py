from django.contrib import admin
from mytweet.models import Tweets, HashTag

# Register your models here.
admin.site.register(Tweets)
admin.site.register(HashTag)
