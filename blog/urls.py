from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('addblog/', views.addblog, name = 'addblog'),
    path('postblog/', views.postblog, name='postblog'),
]
