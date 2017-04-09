# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def index(request):
    books_list = Book.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    query = request.GET.get('q')
    if query:
        books_list = books_list.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)|
            Q(autor__icontains=query)|
            Q(owner__first_name__icontains=query)|
            Q(owner__last_name__icontains=query)
            ).distinct()
    page = request.GET.get('page', 1)
    paginator = Paginator(books_list, 10)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'books':books})

@login_required
def book_detail(request, slug=None):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/books_detail.html', {'book':book})
