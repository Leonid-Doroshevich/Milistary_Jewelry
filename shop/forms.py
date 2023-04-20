from django import forms
from .models import Product

class Quantity(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('quantity',)
        widgets = {
           'quantity': forms.NumberInput(attrs={
                    'class': 'form-control'
           })}
