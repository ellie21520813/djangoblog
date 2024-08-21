from django.urls import path
from .import views
urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('addcontact/', views.addcontact, name='addcontact'),
    path('getcontact/', views.getcontact, name='getcontact'),
    path('postContact/', views.postContact, name= 'postcontact')
]
