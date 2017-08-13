from django.conf.urls import url
from blog.views import *
from django.conf import settings
urlpatterns = [
    url(r'^$',index,name = 'index'),
    url(r'^category/',category,name = 'category'),
    url(r'^tag/',tag,name = 'tag'),
    url(r'^article/',article,name = 'article'),
    url(r'^reg/',reg,name = 'reg'),
    url(r'^login/',login,name = 'login'),
    url(r'^archive/',archive,name = 'archive'),
    url(r'^logout',logout,name = 'logout'),
    url(r'^write_article/',write_article,name = 'write_article'),
]
