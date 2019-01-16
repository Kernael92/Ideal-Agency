# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_model = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


class Model(models.Model):
    LOCATION_CHOICE = (
        ('Mombasa','Mombasa'),
        ('Nairobi','Nairobi'),
        ('Kisumu','Kisumu'),
        ('Nakuru','Nakuru'),
    )

    GENDER_CHOICE = (
        ('F','FEMALE'),
        ('M','MALE'),
    )

    HEIGHT_CHOICE = (
        (190,'190cm'),
        (185,'185cm'),
        (180,'180cm'),
        (175,'175cm'),
        (170,'170cm'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(max_length = 20)
    height = models.IntegerField(choices=HEIGHT_CHOICE, default = 0)
    gender = models.CharField(choices = GENDER_CHOICE,max_length = 7)
    location = models.CharField(choices=LOCATION_CHOICE,max_length = 245)
    photolook = models.ImageField(upload_to='photolook')

    def save_model(self):
        self.save()

    def delete_model(self):
        self.delete()

    def update_model(self,id):
        model = Model.objects.filter(model_id=id).update()
        return model

class Client(models.Model):
    OCCUPATION_FIELD = (
        ('PHOTOGRAPHER','PHOTOGRAPHER'),
        ('FASHION STYLIST','FASHION STYLIST'),
        ('INDUSTRY PROFESSIONAL','INDUSTRY PROFESSIONAL'),
        ('HAIR AND MAKE UP ARTIST','HAIR AND MAKE UP ARTIST'),
        

    )
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    occupation = models.CharField(max_length = 200,choices = OCCUPATION_FIELD)
    phone_number = models.CharField(max_length = 20)

class Casting(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    details = models.TextField()
    image = models.ImageField(upload_to = 'image')
    valid_date = models.DateField(auto_now_add=True)


class Booking(models.Model):
    model = models.ForeignKey(Model,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)



   

