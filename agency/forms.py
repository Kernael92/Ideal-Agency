from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Model,Client,Casting
from django.forms import ModelForm,Textarea, IntegerField


class NewCastingForm(forms.ModelForm):
    class Meta:
        model = Casting
        fields = ['client','Title', 'image','details','valid_date']

class NewModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['model','phone_number','height','gender','location','image','profile_pic','occupation']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client', 'profile_pic','occupation','phone_number']


