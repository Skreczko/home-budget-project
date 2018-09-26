from django import forms
from django.forms import  ModelForm
from .models import Expense , Project

class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.DecimalField(max_digits=8, decimal_places=2)
    category = forms.CharField()

class CategoryForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['category']

class ProjectForm(forms.Form):
    budget = forms.DecimalField(max_digits=8, decimal_places=2)