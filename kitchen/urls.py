from django.urls import path, include

from kitchen.views import index, DishTypeListView, dish_type_detail_view, DishListView, DishDetailView, CookListView

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/<int:pk>/", dish_type_detail_view, name="dish-type-detail"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cooks-list")
]

app_name = "kitchen"
