from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.startpage, name='startpage'),
#    url(r'^user/(\w)/$', Profile.as_view),
]
