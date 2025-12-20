from django.conf import settings
from django.db import models

class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    activity_type = models.CharField(max_length=50) 
    duration = models.IntegerField()                                                           distance = models.FloatField(null=True, blank=True)
    calories_burned = models.IntegerField(null=True, blank=True)
    date = models.DateField()                         
    created_at = models.DateTimeField(auto_now_add=True

    def __str__(self):
        return f"{self.activity_type} by {self.user.username} on {self.date}"

# Create your models here.
