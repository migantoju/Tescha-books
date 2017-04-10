# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

Degree_choices = (
    ("1", 'Ingeniería Informática'),
    ("2", 'Ingeniería en Sistemas Computacionales'),
    ("3", 'Ingeniería Electromecanica'),
    ("4", 'Ingeniería Industrial'),
)
Semestre_choices = (
    ("1", 'Primero'),
    ("2", 'Segundo'),
    ("3", 'Tercero'),
    ("4", 'Cuarto'),
    ("5", 'Quinto'),
    ("6", 'Sexto'),
    ("7", 'Septimo'),
    ("8", 'Octavo'),
    ("9", 'Noveno'),
    ("10", 'Residencias'),
)
def upload_location(instance, filename):
    return "%s/%s" %(instance.matricula, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    degree = models.CharField(max_length=100, choices=Degree_choices)
    matricula = models.CharField(max_length=9)
    pic = models.ImageField(upload_to=upload_location)
    semestre = models.CharField(max_length=100, choices=Semestre_choices)
    created_date = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" %(self.user.first_name)
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
