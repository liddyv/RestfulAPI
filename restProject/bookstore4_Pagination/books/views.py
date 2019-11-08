from rest_framework import generics
from django_filters import FilterSet, NumberFilter
from books.models import Book
from books.serializers import GetBookSerializer, PostBookSerializer, FullBookSerializer
from books.utils.custompagination import BookPagination

class PriceFilter(FilterSet):
    highest_price = NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )

    lowest_price = NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )

    class Meta:
        models = Book
        fields = ('price',)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    pagination_class = BookPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostBookSerializer
        else:
            return GetBookSerializer

    ordering_fields = (
        'price',
        'title'
    )

    search_fields = (
        '^title',
        '=book_type'
    )

    filter_class = PriceFilter


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return PostBookSerializer
        else:
            return FullBookSerializer
