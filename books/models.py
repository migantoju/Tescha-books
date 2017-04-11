# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
# Create your models here.

Book_Type_Choices = (
    ('Programacion', 'Programacion'),
    ('Base de Datos', 'Base de Datos'),
    ("Inteligencia Artificial", 'Inteligencia Artificial'),
    ("Machine Learning", 'Machine Learning'),
)

def upload_location(instance, filename):
    return "%s/%s" %(instance.owner, filename)

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError("Formato de archivo no permitido")

class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    autor = models.CharField(max_length=200)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    files = models.FileField(upload_to=upload_location, validators=[validate_file_extension])
    book_type = models.CharField(max_length=100, choices=Book_Type_Choices)

#Definimos la funcion para publicar el libro
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #Regresa el numero total de likes que tiene un libro
    @property
    def total_likes(self):
        return self.likes.count()
#Mostramos el titulo del libro en un lenguaje humano
    def __unicode__(self):
        return "%s" %(self.title)

    # Aqui va el get_absolute_url
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={'slug': self.slug})
#Creamos una funcion "create_slug" para crear el Slug que se va a guardar
#en la base de datos y a la cual se le asignara a nuestro libro
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Book.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first.id)
        return create_slug(instance, new_slug=new_slug)
    return slug
#Mandamos a llamar el metodo "pre_save" para hacer una funcion antes de
#guardar el slug
def pre_save_book_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_book_receiver, sender=Book)
