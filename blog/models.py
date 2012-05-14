from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        ''' 
        Returns a 'label' for the class, BlogPost, that
        is easily understandable for humans to read.
        '''
        return self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField('Name',max_length=256)
    body = models.TextField('Comment')
    post = models.ForeignKey(BlogPost)

    def __unicode__(self):
        ''' 
        Returns a 'label' for the class, Comment, that
        is easily understandable for humans to read.
        '''
        return unicode("%s: %s" % (self.post, self.body[:60]))
