from django.conf.urls import url
from .views import add_comment_to_book

urlpatterns = [
    url(r'^add_comment/(?P<pk>\d+)/$', add_comment_to_book, name='add_comment_to_book'),
]
