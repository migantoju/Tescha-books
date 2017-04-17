# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, Category
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'owner', 'files')
    search_fields = ["title", "autor"]
    ordering = ["title"]

admin.site.register(Book, BookAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ["title"]
    ordering = ['title']

admin.site.register(Category, CategoryAdmin)
