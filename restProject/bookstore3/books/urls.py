from django.conf.urls import url
from books.views import BookList, BookDetail, CommentList, CommentDetail, RatingCreate

urlpatterns = [
    url(
        r'^books$',
        BookList.as_view(),
        name=BookList.name
    ),
    url(
        r'^books/(?P<pk>[0-9]+)$',
        BookDetail.as_view(),
        name=BookDetail.name
    ),
    url(
        r'^comments$',
        CommentList.as_view(),
        name=CommentList.name
    ),
    url(
        r'^comments/(?P<pk>[0-9]+)$',
        CommentDetail.as_view(),
        name=CommentDetail.name
    ),
    url(
        r'^ratings$',
        RatingCreate.as_view()
    )

]