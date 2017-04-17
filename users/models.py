# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Degree(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=200, verbose_name='Title')

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __unicode__(self):
        return '%s' %(self.title)

class Semestre(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=200, verbose_name='Title')

    class Meta:
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"


    def __unicode__(self):
        return '%s' %(self.title)

def upload_location(instance, filename):
    return "%s/%s" %(instance.matricula, filename)

from stdimage.models import StdImageField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    degree = models.ForeignKey(Degree, verbose_name='Carrera', null=True, blank=True)
    matricula = models.CharField(max_length=9)
    # pic = models.ImageField(upload_to=upload_location, default='default.png')
    pic = StdImageField(upload_to=upload_location, default='default.png', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })
    semestre = models.ForeignKey(Semestre, verbose_name='Semestre', null=True, blank=True)
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
