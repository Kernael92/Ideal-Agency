# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from .models import Model,Client,Casting
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .decorators import model_required,client_required
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    
    return render(request,'index.html')

def SignUpView(request):
    return render(request,'registration/sign.html')



def model(request):
    models = Model.objects.all()
    return render(request,'agency/model.html',{'models':models})

def casting(request):
    castings = Casting.objects.all()
    return render(request,'agency/casting.html',{'castings':castings})





