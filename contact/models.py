from django.db import models

# Create your models here.
class Contactlist(models.Model):
    username = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    body = models.TextField(max_length=1024, default='')