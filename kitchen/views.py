from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    count_dishes = Dish.objects.count()
    count_cooks = get_user_model().objects.count()
    count_dish_types = DishType.objects.count()
    context = {
        "count_dishes": count_dishes,
        "count_cooks": count_cooks,
        "count_dish_types": count_dish_types
    }
    return render(request, "kitchen/index.html", context)
