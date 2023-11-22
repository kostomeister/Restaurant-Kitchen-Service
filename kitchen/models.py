from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=64)


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()


class Dish(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(
        get_user_model(), related_name="dishes"
    )
