from django import forms
from django.contrib.auth import get_user_model

from .models import DishType, Dish


class DishTypeCreateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ['name']


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"
