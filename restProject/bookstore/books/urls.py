from django.conf.urls import url
#from books.views import BookList, BookDetail
from books.views import book_list, book_detail

urlpatterns = [
    url(
        r'^books$',
        #BookList.as_view()
        book_list
    ),
    url(
        r'^books/(?P<pk>[0-9]+)$',
        #BookDetail.as_view()
        book_detail
    )
]