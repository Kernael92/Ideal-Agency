from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Model,Client,User

class ModelSignUpForm(UserCreationForm):
    fields = ['location','gender','height','phone_number']

    class Meta(UserCreationForm.Meta):
        model = User

        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.is_model = True
            user.save()
            model = Model.objects.create(user=user)
            model.location.add(*self.cleaned_data.get('location'))
            model.gender.add(*self.cleaned_data.get('gender'))
            model.height.add(*self.cleaned_data.get('height'))
            return user



