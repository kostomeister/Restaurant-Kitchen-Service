from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishTypeCreateForm, DishForm
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


def dish_type_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    dish_type = get_object_or_404(DishType, pk=pk)
    dishes = dish_type.dish_set.all()

    context = {
        'dish_type': dish_type,
        'dishes': dishes,
    }

    return render(request, 'kitchen/dish_type_detail.html', context)


class DishTypeCreateView(generic.CreateView):
    model = DishType
    form_class = DishTypeCreateForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    form_class = DishTypeCreateForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 3


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = DishType
    form_class = DishForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class CookListView(generic.ListView):
    model = get_user_model()
    paginate_by = 3


class CookDetailView(generic.DetailView):
    model = get_user_model()
