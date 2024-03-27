from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Job


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company', 'location', 'requirements']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control'}),
        }

class JobSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100, required=False)

class HomeSearchForm(forms.Form):
    search_query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search for jobs...'}))