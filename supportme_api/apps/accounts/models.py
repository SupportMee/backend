
from django.db import models

# User

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256,unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name + " " + self.last_name
