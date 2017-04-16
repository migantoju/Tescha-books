# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Comment(models.Model):
    book = models.ForeignKey('books.Book', related_name='comments')
    user = models.ForeignKey(User, unique=False)
    text = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approved(self):
        self.approved_comment = True
        self.save()

    def __unicode__(self):
        return self.user.username

def approved_comments(self):
    return self.comments.filter(approved_comment=True)
