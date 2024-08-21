from django.contrib import admin
from .models import post_blog, Comment
# Register your models here.
admin.site.register(post_blog)
admin.site.register(Comment)
