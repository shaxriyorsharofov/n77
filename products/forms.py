from django import forms
from .models import Category, Cars

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"
        
        