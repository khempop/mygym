from django.db import models
from django.contrib.auth.models import AbstractUser

from gym.models import *

from django.db import models
from django.contrib.auth.models import Group, User

class Gym(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(('email address'), unique = True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    firstname = models.CharField(max_length=100, blank=True, default='')
    lastname = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField(blank=True, default='')
    stripeid = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)
    class Meta:
        ordering = ['created']

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField(blank=True, default='')
    email = models.EmailField(blank=True, default='')
    stripeid = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']