from django.conf import settings
from django.db import models

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    target_date = models.DateField(null=True, blank=True)
    achieved = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
# Create your models here.
