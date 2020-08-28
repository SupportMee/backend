
from django.db import models
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User as make_password
# User

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256,unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name + " " + self.last_name
