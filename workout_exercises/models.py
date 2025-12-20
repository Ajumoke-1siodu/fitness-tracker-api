from django.conf import settings
from django.db import models


class WorkoutExercise(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout = models.ForeignKey('workouts.Workout', on_delete=models.CASCADE, null=True, blank=True)
    exercise_name = models.CharField(max_length=100, null=True, blank=True)
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    weights = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.exercise_name} - {self.user.username} - {self.workout}"

