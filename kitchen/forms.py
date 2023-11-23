from django import forms
from django.contrib.auth import get_user_model

from .models import DishType, Dish


class DishTypeForm(forms.ModelForm):
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


class DishTypeSearchForm(forms.Form):
    dish_type = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search by Dish Type"}),
        label="",
        required=False
    )


class DishSearchForm(forms.Form):
    dish_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search Dish by name"}),
        label="",
        required=False
    )


class CookSearchForm(forms.Form):
    cook_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search Cook by name"}),
        label="",
        required=False
    )
