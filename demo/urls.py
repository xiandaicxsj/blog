from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
url(r'^admin/', include(admin.site.urls)),url(r'^ar/$',archive),
url(r'^blog/(?P<id>\d+)/$',blog_show,name='blog_show'),url(r'^change/(?P<id>\d+)/$',blog_change,name='blog_ch'),(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS}),)
urlpatterns +=staticfiles_urlpatterns()
