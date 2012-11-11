from blog.models import BlogPost, Comment
from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
	'''
	Displays what you want seen in the Admin dashboard for comments.
	'''
	list_display = ["post", "author", "created"]

class BlogPostAdmin(admin.ModelAdmin):
	'''
	Displays what you want seen in the Admin dashboard for blog posts.
	'''
	def preview(self, obj):
		return obj.body[0:100]

	list_display = ["title", "author", "preview"]
	search_fields = ["title"]

# registers both the models and the admin displays for 
# the admin site
admin.site.register(Comment, CommentAdmin)
admin.site.register(BlogPost, BlogPostAdmin)