from django.urls  import path, include
from .import views
urlpatterns = [
    path('', views.homelog, name='home'),
    path('detail/<int:id>', views.detailpost, name ='detailpost'),
]
