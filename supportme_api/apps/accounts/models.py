from django.db import models
#from django.contrib.auth.models import User as UserModel

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name + " " + self.last_name
