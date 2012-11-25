from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'MyBlog.views.home', name='home'),
	url(r'^(\d+)/$', 'MyBlog.views.post', name='post'),
    url(r'^admin/', include(admin.site.urls)),
)
