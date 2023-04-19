from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm 
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter your login'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your passord'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter your login'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter your email'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your passord'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Repeat your passord'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    postcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'readonly': True}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'address', 'city', 'postcode', 'state', 'email', 'username', 'image')