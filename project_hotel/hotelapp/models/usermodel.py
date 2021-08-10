from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(models.Model):
    """
    A User.
    """
    GENRES_CHOICES = (
        ('F', 'F'),
        ('M', 'M'),
    )

    username = models.CharField(max_length=30, null=True)
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    phone = models.CharField(('phone'), max_length=255, null=True)
    sexe = models.CharField(('genre'), max_length=255, null=True, choices=GENRES_CHOICES)
    profile_pic = models.ImageField(default="profile2.png", null=True, blank=True, upload_to='profil/')
    type_user = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    image_profil = models.ImageField(default="profile1.png", null=True)
    creation_date = models.DateTimeField( auto_now_add=True)
    modification_date = models.DateTimeField( auto_now=True)

    class Meta:
        verbose_name = ('Utilisatur')
        verbose_name_plural = ('Utilisateurs')

    def __str__(self):
        return self.username
    
    def register(self):
        self.save()

    @property
    def imageURL(self):
        try:
            url = self.image_profil.url
        except:
            url = ''
        return url

    @staticmethod
    def get_user_model_by_email(email):
        try:
            return UserModel.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if UserModel.objects.filter(email=self.email):
            return True

        return False