from django.db import models
from users.models import User  
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Property(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='inquiries')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.property.title} by {self.user.username}"