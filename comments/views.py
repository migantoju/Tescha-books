# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Comment
from books.models import Book
from .forms import CommentForm
# Create your views here.
@login_required
def add_comment_to_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.user = request.user
            comment.save()
            return redirect('book_detail', slug=book.slug)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment_to_book.html', {'form':form})
