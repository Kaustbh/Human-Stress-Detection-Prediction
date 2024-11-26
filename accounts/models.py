from django.db import models
from django.contrib.auth.models import User
# from django.conf.urls import url
from django.urls import re_path
from django.shortcuts import resolve_url


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # profile_pic = models.ImageField(upload_to='profile_pics', default="1.jpg")

    def __str__(self):
        return self.user.username
    
    class Meta:
        abstract = True

class ConcreteUserProfile(UserProfileInfo):
    # Add any additional fields if necessary
    pass

# Create your models here.
