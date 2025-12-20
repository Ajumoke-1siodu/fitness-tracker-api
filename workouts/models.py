from django.conf import settings
from django.db import models

class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_type = models.ForeignKey('workout_types.workoutType', on_delete=models.SET_NULL, null=True, blank=True)
    workout_name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.workout_name} - {self.user.username}"
# Create your models here.
