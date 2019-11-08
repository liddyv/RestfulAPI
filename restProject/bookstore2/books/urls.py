from django.conf.urls import url
from books.views import book_list, book_detail

urlpatterns = [
    url(
        r'^books$',
        book_list
    ),
    url(
        r'^books/(?P<pk>[0-9]+)$',
        book_detail
    )
]