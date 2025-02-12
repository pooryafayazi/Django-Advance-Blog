from django.db import models
from django.contrib.auth import get_user_model
# from accounts.models import Profile
# Create your models here.

# get_user_model objects
# User = get_user_model()

class Post (models.Model):
    '''
    Post model for blog app
    '''
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.title


class Category(models.Model):
    '''
    Category model for blog app
    '''
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name