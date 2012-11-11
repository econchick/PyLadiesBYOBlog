from blog.views import BlogView, SinglePost, AddComment
#from blog.models import BlogPost
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', BlogView.as_view(template_name='list.html'), name='blogview'),
	url(r'^(?P<pk>\d+)/$', SinglePost.as_view(template_name='post_detail.html'),  name='singlepost'),
	#url(r'^(?P<pk>\d+)/comment', AddComment.as_view(template_name='comment_form.html'), name='commenturl'),
)
