from blog.models import Comment
from django import forms
from django.forms import ModelForm, Textarea

class CommentForm(ModelForm):
	'''
	Builds a comment form based off of the Comment model.
	'''
	class Meta:
		model = Comment
		fields = ('author', 'body')
		widgets = {
            'body': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
