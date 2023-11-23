from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishTypeForm, DishForm, DishTypeSearchForm, DishSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        dish_type = self.request.GET.get("dish_type", "")
        context["dish_type_search_form"] = DishTypeSearchForm(
            initial={"dish_type": dish_type}
        )
        return context

    def get_queryset(self):
        dish_type = self.request.GET.get("dish_type")
        queryset = DishType.objects.all()
        if dish_type:
            queryset = queryset.filter(name__icontains=dish_type)
        return queryset


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
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        dish_name = self.request.GET.get("dish_name", "")
        context["dish_name_search_form"] = DishSearchForm(
            initial={"dish_name": dish_name}
        )
        return context

    def get_queryset(self):
        dish_name = self.request.GET.get("dish_name")
        queryset = Dish.objects.all()
        if dish_name:
            queryset = queryset.filter(name__icontains=dish_name)
        return queryset


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dishes-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dishes-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")


class CookListView(generic.ListView):
    model = get_user_model()
    paginate_by = 3
    queryset = get_user_model().objects.filter(is_staff=True)


class CookDetailView(generic.DetailView):
    model = get_user_model()
