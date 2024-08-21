from django.db import models

# Create your models here.
class imageblogmodel(models.Model):
    blog_title= models.CharField(max_length=255, default='')
    blog_image = models.FileField()
    blog_body = models.TextField()