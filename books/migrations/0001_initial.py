# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 21:18
from __future__ import unicode_literals

import books.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('autor', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('files', models.FileField(upload_to=books.models.upload_location, validators=[books.models.validate_file_extension])),
                ('book_type', models.CharField(choices=[('Programacion', 'Programacion'), ('Base de Datos', 'Base de Datos'), ('Inteligencia Artificial', 'Inteligencia Artificial'), ('Machine Learning', 'Machine Learning')], max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
