from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user_ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
# Create your models here.
