from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=64)


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()


