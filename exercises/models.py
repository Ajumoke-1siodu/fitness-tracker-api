from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    muscle_group = models.CharField(max_length=50, null=True, blank=True)
    equipment = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
# Create your models here.
