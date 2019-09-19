from django import forms
from django.forms import widgets
from webapp.models import category


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=2000, required=True, label='Details', widget=widgets.Textarea)
    category = forms.ChoiceField(required=False, label='Category', initial="New", choices=category)
    count = forms.IntegerField(required=False, label='Count', min_value=0)
    price = forms.DecimalField(required=True, max_digits=7, label='Price', decimal_places=2)

