# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    try:
        books = paginator.page('page')
    except PageNotAnInteger:
        # Si la pagina no es un numero entero, regresara a la primara pagina
        books = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            #Si la peticion es via ajax y la pagina esta fuera de rango, retornara una pagina vacia
            return HttpResponse('')
        #Si la pagina esta fuera de rango, regresara a la ultima pagina con resultados
        books = paginator.page(pagina.num_pages)
    if request.is_ajax():
        return render(request, 'books/list_ajax.html', {'books':books})
    return render(request, 'index.html', {'books':books})

@login_required
def book_detail(request, slug=None):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/books_detail.html', {'book':book})
