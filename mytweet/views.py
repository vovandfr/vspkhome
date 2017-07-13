from django.views.generic import View
from django.shortcuts import render
from mytweet.models import Tweets
from django.contrib.auth.models import User


# Create your views here.
class Index(View):
    def get(self, request):
        params = {}
        params['name'] = "Django"
        return render(request, 'tweets/base.html', params)


class Profile(View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweets.objects.filter(user=user)
        params['tweets'] = tweets
        params['user'] = user
        return render(request, 'tweets/profile.html', params)
