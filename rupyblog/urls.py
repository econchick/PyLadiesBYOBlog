from django.conf.urls import patterns, include, url
from django.contrib import admin

from ZieBlog import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^(\d+)/$', views.post, name='post'),
    url(r'^admin/', include(admin.site.urls)),
)
