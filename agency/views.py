# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Model,Client,User
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import ModelSignUpForm


# Create your views here.
def index(request):
    
    return render(request,'index.html')

def SignUpView(request):
    return render(request,'registration/sign.html')

class ModelSignUpView(CreateView):
    model = User
    form_class = ModelSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'model'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('models')

