from django.db import models
from django.contrib import admin

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

admin.site.register(UserInfo)
