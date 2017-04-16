# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import CreateView
from .forms import New_Book_Form
from django.contrib.auth.models import User

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

from comments.forms import CommentForm
from comments.models import Comment

@login_required
def book_detail(request, slug=None):
    book = get_object_or_404(Book, slug=slug)
    comments = Comment.objects.all()
    form = CommentForm()
    return render(request, 'books/books_detail.html', {'book':book, 'form':form, 'comments':comments})

@login_required
def UploadBook(request):
    saved = False
    if request.method == 'POST':
        form = New_Book_Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            # book.published_date = timezone.now()
            book.owner = request.user
            book.save()
            saved = True
            form.save_m2m()
            return redirect('/')
    else:
        form = New_Book_Form()
    return render(request, 'books/upload_form.html', {'form':form})

@login_required
def book_edit(request, slug=None):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = New_Book_Form(request.POST or None, request.FILES or None, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_detail', slug=slug)
    else:
        form = New_Book_Form(instance=book)
    return render(request, 'books/book_edit.html', {'form':form})

@login_required
def book_remove(request, slug=None):
    book = get_object_or_404(Book, slug=slug)
    book.delete()
    return redirect('/')

@login_required
def book_draft_list(request):
    book = Book.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'books/book_draft_list.html', {'book': book})

@login_required
def book_publish(request, slug=None):
    book = get_object_or_404(Book, slug=slug)
    book.publish()
    return redirect('book_detail', slug=slug)

from comments.models import Comment

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approved()
    return redirect('book_detail', slug=comment.book.slug)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    book_pk = comment.book.slug
    comment.delete()
    return redirect('book_detail', slug=book_pk)
