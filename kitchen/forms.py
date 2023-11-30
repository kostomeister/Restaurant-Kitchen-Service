from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import DishType, Dish


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
            "is_staff",
        )


class DishTypeSearchForm(forms.Form):
    dish_type = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search by Dish Type"}),
        label="",
        required=False,
    )


class DishSearchForm(forms.Form):
    dish_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search Dish by name"}),
        label="",
        required=False,
    )


class CookSearchForm(forms.Form):
    cook_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search Cook by name"}),
        label="",
        required=False,
    )


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class CookUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email", "years_of_experience")
