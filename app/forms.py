from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django.http import request
from django.shortcuts import redirect
from .models import *

class BookForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NAME'}))
    author =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AUTHOR'}))
    ISBN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}))
    publication_year = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PUBLICATION_YEAR'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PRICE'}))
    status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'STATUS: available, borrowed'}))
    class Meta:
        model = Book
        fields = '__all__'

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username',  'email')

class PasswordUpdateForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'




class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 're-enter password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email address'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'

