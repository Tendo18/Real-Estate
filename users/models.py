from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.
#Define the User roles
class User(AbstractUser):
    ROLE = (
        ('agent', 'Agent'),
        ('client', 'Client'),
    )       

    #extend the user model with additional fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE, default='client')
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
        

