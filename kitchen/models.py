from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=64)


