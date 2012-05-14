from blog.forms import CommentForm
from blog.models import BlogPost, Comment
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.db import models
from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


def add_comment(request, pk):
    """
    Add a new comment.
    """
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]
        comment = Comment(post=Post.objects.get(pk=pk))

        # save comment form
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False
        comment = cf.save(commit=False)

        # save comment instance
        comment.author = author
        notify = True
        if request.user.username == "ak": notify = False
        comment.save(notify=notify)
    return HttpResponseRedirect(reverse("dbe.blog.views.post", args=[pk]))

class BlogView(ListView):
    model = BlogPost
    paginate_by = 2
    context_object_name = 'post_list'
    template_name = 'list.html'

    def get_queryset(self):
        queryset = BlogPost.objects.all().order_by('-created');
        return queryset


    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)


class SinglePost(DetailView):
    """
    Single post with comments.
    """
    template_name = "post_detail.html"
    model = BlogPost
    context_object_name = "single_post"

    def get(self, request, *args, **kwargs):
        super(DetailView, self).get(request, *args, **kwargs)

        context = self.get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=kwargs['pk']).order_by('-created')

        return self.render_to_response(context)


class AddComment(CreateView):
    """ 
    Adds a new comment.
    """
    success_url = "/"
    model = BlogPost
    form_class = CommentForm
    template_name = 'comment_form.html'
    context_object_name = 'add_comment'

    def form_valid(self, form):
        post = BlogPost.objects.get(pk=self.args[0])
        comment, created = Comment.objects.get_or_create(post=post)
        self.object = form.save(commit=False)
        if not form.author:
            self.object.author = 'Anonymous'
        self.object.save()
        return super(CreateView, self).form_valid(form)




