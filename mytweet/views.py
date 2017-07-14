from django.views.generic import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.template import Context
import json
from .models import Tweets, HashTag
from .forms import TweetForm, SearchForm


# Create your views here.
class Index(View):
    def get(self, request):
        params = {}
        params['name'] = "Django"
        return render(request, 'tweets/base.html', params)


class Error(View):
    def get(self, request):
        params = {}
        return render(request, 'tweets/error.html', params)


class Profile(View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweets.objects.filter(user=user)
        form = TweetForm()
        params['tweets'] = tweets
        params['user'] = user
        params['form'] = form
        return render(request, 'tweets/profile.html', params)


class PostTweet(View):
    """Tweet Post form available on page /user/<username> URL"""
    def post(self, request, username):
        form = TweetForm(data=self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            tweet = Tweets(text=form.cleaned_data['text'],
                           user=user,
                           country='Albania')
            tweet.save()
            words = form.cleaned_data['text'].split(' ')
            for word in words:
                if word[0] == '#':
                    hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.tweet.add(tweet)
            return HttpResponseRedirect(reverse('tweets:profile', args=[username]))
        else:
            return HttpResponseRedirect(reverse('tweets:error'))


class HashTagCloud(View):
    """User HashTagCloud page reachable from /hashtag/<hashtag> URL"""
    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params['tweets'] = hashtag.tweet
        return render(request, 'tweets/hashtagcloud.html', params)


class Search(View):
    """Search all tweets with query /search/?query=<query> URL"""
    def get(self, request):
        form = SearchForm()
        params = dict()
        params['search'] = form
        return render(request, 'tweets/search.html', params)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets = Tweets.objects.filter(text__icontains=query)
            context = Context({'query': query, 'tweets': tweets})
            return_str = render_to_string('tweets/partials/_tweet_search.html',
                                          context)
            return HttpResponse(json.dumps(return_str),
                                content_type="application/json")
        else:
            HttpResponseRedirect(reverse('tweets/search.html'))
