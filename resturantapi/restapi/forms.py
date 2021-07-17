from .models import Menu
from django import forms

class FoodForm(forms.ModelForm):
    class Meta:
        model=Menu
        fields=['mealname','price']