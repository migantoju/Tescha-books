# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Degree, Semestre
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'degree', 'matricula', 'semestre')
    search_fields = ["user__username", "matricula"]
    ordering = ["user"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Degree)
admin.site.register(Semestre)
