# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Model(models.Model):
    LOCATION_CHOICE = (
        ('Mombasa','Mombasa'),
        ('Nairobi','Nairobi'),
        ('Kisumu','Kisumu'),
        ('Nakuru','Nakuru'),
    )

    GENDER_CHOICE = (
        ('FEMALE','FEMALE'),
        ('MALE','MALE'),
    )

    HEIGHT_CHOICE = (
        (190,'190cm'),
        (185,'185cm'),
        (180,'180cm'),
        (175,'175cm'),
        (170,'170cm'),
    )
    OCCUPATION_FIELD = (
        ('MODEL','MODEL'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(max_length = 20)
    height = models.IntegerField(choices=HEIGHT_CHOICE, default = 0)
    gender = models.CharField(choices = GENDER_CHOICE,max_length = 7)
    location = models.CharField(choices=LOCATION_CHOICE,max_length = 245)
    image = models.ImageField(upload_to='photolook')
    profile_pic = models.ImageField(upload_to = 'profile_pic', null='True')
    occupation = models.CharField(max_length = 200,choices = OCCUPATION_FIELD)

    def save_model(self):
        self.save()

    def delete_model(self):
        self.delete()

    def update_model(self,id):
        model = Model.objects.filter(model_id=id).update()
        return model

    def __str__(self):
        return self.user.username


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
    profile_pic = models.ImageField(upload_to='profile_pic',null=True)

    def save_client(self):
        self.save()

    def delete_client(self):
        self.delete()

    def update_client(self,id):
        client = Client.objects.filter(client_id=id).update()
        return client

    def __str__(self):
        return self.user.username


class Casting(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    Title=models.CharField(max_length=245, null=True)
    details = models.TextField()
    image = models.ImageField(upload_to = 'image')
    valid_date = models.DateField(auto_now_add=True)

    def save_casting(self):
        self.save()

    def delete_casting(self):
        self.delete()

    def update_casting(self,id):
        casting = Casting.objects.filter(client_id=id).update()
        return casting

    def __str__(self):
        return self.Title

    


class Booking(models.Model):
    model = models.ForeignKey(Model,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)



   

