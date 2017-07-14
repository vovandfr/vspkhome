"""Defined URL patterns for learning_logs."""

from django.conf.urls import url

from .views import Index, Error, Profile, PostTweet, HashTagCloud, Search

urlpatterns = [
    # Homepage
    url(r'^$', Index.as_view(), name='index'),
    url(r'^user/(\w+)$', Profile.as_view(), name='profile'),
    url(r'^user/(\w+)/post/$', PostTweet.as_view(), name='posttweet'),
    url(r'^hashtag/(\w+)$', HashTagCloud.as_view(), name='hashtagcloud'),
    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^error/$', Error.as_view(), name='error'),
]
