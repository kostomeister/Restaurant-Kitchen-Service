from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

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


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 6


def dish_type_detail_view(request, pk):
    dish_type = get_object_or_404(DishType, pk=pk)
    dishes = dish_type.dish_set.all()

    context = {
        'dish_type': dish_type,
        'dishes': dishes,
    }

    return render(request, 'kitchen/dish_type_detail.html', context)


