import os

from django.db import models

from apps.classification.models import Category, City
from apps.accounts.models import User
# Create your models here.


def get_upload_to(instance, filename):
    folder_name = 'huecas'
    return os.path.join(folder_name, str(instance.id), filename)


class Hueca(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    phone = models.PhoneNumberField(blank=True)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
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
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(
        upload_to=get_upload_to, width_field='width', height_field='height')
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
