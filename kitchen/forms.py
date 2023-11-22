from django import forms
from .models import DishType


class DishTypeCreateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ['name']
