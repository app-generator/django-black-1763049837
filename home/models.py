# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Usuario(models.Model):

    #__Usuario_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    contraseña = models.CharField(max_length=255, null=True, blank=True)
    esadmin = models.BooleanField()

    #__Usuario_FIELDS__END

    class Meta:
        verbose_name        = _("Usuario")
        verbose_name_plural = _("Usuario")


class Imagen(models.Model):

    #__Imagen_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    titulo = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    ruta = models.CharField(max_length=255, null=True, blank=True)
    publicada = models.BooleanField()

    #__Imagen_FIELDS__END

    class Meta:
        verbose_name        = _("Imagen")
        verbose_name_plural = _("Imagen")



#__MODELS__END
