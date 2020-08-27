from django.db import models

from apps.accounts.models import User
from apps.hueca.models import Hueca

# Create your models here.

class Like(models.Model):
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.hueca+":"+self.user


class Rating(models.Model):
    score=models.IntegerField()
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.score


class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hueca+":"+self.user
