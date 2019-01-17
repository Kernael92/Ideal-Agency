from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Model,Client,Casting
from django.forms import ModelForm,Textarea, IntegerField


class NewCastingForm(forms.ModelForm):
    class Meta:
        model = Casting
        fields = ['client','Title', 'image','details']

class NewModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['user','phone_number','height','gender','location','image','profile_pic','occupation']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'profile_pic','occupation','phone_number']


