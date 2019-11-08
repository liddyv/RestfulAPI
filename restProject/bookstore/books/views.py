

from books.models import  import Book
from books.serializers import BookSerializer

def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many = True)
        book_data = book_serializer.data
        book_contect = JSONRenderer().render(book_data)
        headers = {'content_type': 'application/json'}
        return HttpResponse(book_contect)
    elif request.method == 'POST':
        pass

def book_detail(request) :

'''
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
'''