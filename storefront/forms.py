from django import forms
from django.forms import ModelForm

from .models import Order


class OrderForm(forms.Form):
    """ Order Form page. Will be replaced by store possibly. """
    class Meta:
        model = Order
        fields = '__all__'
