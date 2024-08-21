from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS =((0,"Draft"), (1,"Published"))
class post_blog(models.Model):
    title_blog= models.CharField(max_length=255, unique=True)
    #slug_blog= models.SlugField(max_length=255, unique=True)
    author_blog = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content_blog = models.TextField()
    blog_image = models.FileField(default="")
    status_blog = models.IntegerField(choices=STATUS, default=0)
class meta(models.Model):
    odering=['-created_on']
def __str__(self):
    return self.title_blog
class Comment(models.Model):
    post = models.ForeignKey(post_blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)