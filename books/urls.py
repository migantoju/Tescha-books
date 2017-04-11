from django.conf.urls import url
from .views import index, book_detail, UploadBook, like_count_book
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^book-detail/(?P<slug>[\w-]+)/$', book_detail, name='book_detail'),
    url(r'^upload/$', UploadBook, name='UploadBook'),
    url(r'^like-book/$', like_count_book, name='like_count_book'),
]
