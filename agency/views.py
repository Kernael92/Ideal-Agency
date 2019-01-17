# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from .models import Model,Client,Casting
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .decorators import model_required,client_required
from django.contrib.auth.models import User
from .forms import NewCastingForm,NewModelForm,ClientForm


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

@login_required
def new_casting(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewCastingForm(request.POST, request.FILES,)
        if form.is_valid():
            casting = form.save(commit = False)
            casting.user = current_user
            casting.save()
        return redirect ('casting')
    else:
        form = NewCastingForm()
    return render(request, 'new_casting.html', {'form': form})


@login_required
def new_model(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewModelForm(request.POST, request.FILES,)
        if form.is_valid():
            model = form.save(commit = False)
            model.user = current_user
            model.save()
        return redirect ('model')
    else:
        form = NewModelForm()
    return render(request, 'new_model.html', {'form': form})


