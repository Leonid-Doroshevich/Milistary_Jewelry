from django import forms
from contact.models import Message

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control'
                }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter e-mail',
                'class': 'form-control'
                }
        )
    )    
    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter your message',
                'class': 'form-control'
                }
        )
    )
