from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=40,blank=False,default='')
    pwd = models.CharField(max_length=40,blank=False,default='')
