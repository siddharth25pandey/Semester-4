from django import forms
from django.contrib.auth.models import User
from . import models


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Roll = forms.CharField(max_length=30)
    Branch = forms.CharField(max_length=30)
    College = forms.CharField(max_length=30)
    Max_sub = forms.CharField(max_length=30)
    Sub1 = forms.CharField(max_length=30)
    Sub2 = forms.CharField(max_length=30)
    Sub3 = forms.CharField(max_length=30)
    Sub4 = forms.CharField(max_length=30)
    Sub5 = forms.CharField(max_length=30)