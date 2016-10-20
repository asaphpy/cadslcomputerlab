from django.conf.urls import patterns, include, url


urlpatterns = patterns('cadsl.index.views',
    url(r'^$', 'home', name='home'),
)