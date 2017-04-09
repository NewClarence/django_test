from django.db import models
from django.contrib import admin

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

admin.site.register(UserInfo)