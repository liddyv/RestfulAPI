from django.conf.urls import url
from books.views import BookList, BookDetail

urlpatterns = [
    url(
        r'^books$',
        BookList.as_view()
    ),
    url(
        r'^books/(?P<pk>[0-9]+)$',
        BookDetail.as_view()
    )
]
