from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter your first name',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter your last name',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Create your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Re-enter your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

