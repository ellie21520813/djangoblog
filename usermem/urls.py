from django.urls import path
from .import views
urlpatterns = [
    path('', views.loginpage.as_view(), name = 'login'),
    path('registeruser/', views.registeruser.as_view(), name='registeruser'),
    path('logout', views.logoutuser, name= 'logout')
]
