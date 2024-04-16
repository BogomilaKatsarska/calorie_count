from django.contrib.auth.models import User
from django.db import models


class Food(models.Model):
    NAME_MAX_LEN = 100
    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name


class Consume(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    food_consumed = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
    )