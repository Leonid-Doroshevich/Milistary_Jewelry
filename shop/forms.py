from django import forms
from .models import Product

class Quantity(forms.ModelForm):
    quantity = forms.IntegerField()
    class Meta:
        model = Product
        fields = ('quantity',)
