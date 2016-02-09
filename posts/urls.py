from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^posts/(?P<slug>.+?)/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^posts/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^projects$', views.projects, name='projects'),
url(r'^blog$', views.blog, name='blog'),
]
