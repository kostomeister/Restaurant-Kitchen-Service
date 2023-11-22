from django.urls import path, include

from kitchen.views import index

urlpatterns = [
    path("", index, name="index")
]

app_name = "kitchen"
