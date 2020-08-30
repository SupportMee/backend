import os

from django.db import models

from apps.classification.models import Category, City
from django.contrib.auth.models import User

# Hueca, Menu, Image

def get_upload_to(instance, filename):
    folder_name = 'huecas'
    #print(instance.hueca_id)
    return os.path.join(folder_name, str(instance.hueca_id), filename)

def get_upload_to_menu(instance, filename):
    folder_name = 'menus'
    #print(instance.hueca_id)
    return os.path.join(folder_name, str(instance.hueca_id), filename)


class Hueca(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15,blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(
        upload_to=get_upload_to_menu)
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(
        upload_to=get_upload_to)
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.image)
    
