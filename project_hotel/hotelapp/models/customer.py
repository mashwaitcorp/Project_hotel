from django.db import models
from django.contrib.auth.models import User
from .usermodel import UserModel


# Create your models here.
class Customer(UserModel):
    """docstring for  Customer"""
    regularite = models.IntegerField(default=0,blank=True)
    #user = models.OneToOneField(UserModel, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "- Client"
        verbose_name_plural = "- Clients"
        ordering = ['regularite']




