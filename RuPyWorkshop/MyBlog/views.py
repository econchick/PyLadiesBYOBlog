# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from MyBlog.models import Post

def home(request):
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 5)

	try:
		page = int(request.GET.get("page", 1))
	except ValueError:
		page = 1

	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)

	return render_to_response("list.html", dict(posts=posts, user=request.user))


def post(request, pk):
	post = Post.objects.get(pk=int(pk))
	return render_to_response("post.html", dict(post=post, user=request.user))




