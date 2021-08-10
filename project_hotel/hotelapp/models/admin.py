from django.db import models
from .usermodel import UserModel


class Admin(UserModel):
    class Meta:
        verbose_name = ('Admin')
        verbose_name_plural = ('Admins')

    def __unicode__(self):
        return u'%s' % self.name


