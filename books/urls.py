from django.conf.urls import url
from .views import index, book_detail, UploadBook, book_edit, book_remove
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^book-detail/(?P<slug>[\w-]+)/$', book_detail, name='book_detail'),
    url(r'^upload/$', UploadBook, name='UploadBook'),
    url(r'^(?P<slug>[\w-]+)/edit/$', book_edit, name='book_edit'),
    url(r'^(?P<slug>[\w-]+)/remove/$', book_remove, name='book_remove'),
]
