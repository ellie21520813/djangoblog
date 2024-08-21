from django.urls import path
from .import views
urlpatterns = [
    path('', views.listproduct, name='listproduct'),
]
