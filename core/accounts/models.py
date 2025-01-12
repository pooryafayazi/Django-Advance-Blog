from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from django.utils.translation import gettext_lazy as _
# Create your models here.
class UserManager(BaseUserManager):
    '''
    Custom User Manager class
    '''
    def create_user(self, email, password, **extra_fields):
        '''
        Create and return a user with email and password
        '''
        if not email:
            raise ValueError(_('Email is required'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''
        Create and return a superuser with email and password
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))        

        return self.create_user(email, password, **extra_fields)




class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom User model with email as unique identifier
    '''
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     return self.is_superuser

    # def has_module_perms(self, app_label):
    #     return True

    # def get_full_name(self):
    #     return self.name

    # def get_short_name(self):
    #     return self.name

    # class Meta:
    #     db_table = 'users'
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'