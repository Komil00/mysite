from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True,blank=True)
    address = models.CharField(max_length=100)
    job = models.CharField(max_length=50)

