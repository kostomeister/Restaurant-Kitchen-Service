from django.urls import path, include

from kitchen.views import (
    index,
    DishTypeListView,
    dish_type_detail_view,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    register_view,
    CookCreateView,
    CookUpdateView,
    CookDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/<int:pk>/", dish_type_detail_view, name="dish-type-detail"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/сreate/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cooks-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cooks-delete"),
    path("cooks/create/", CookCreateView.as_view(), name="cooks-create"),
    path("register/", register_view, name='register')
]

app_name = "kitchen"
