from rest_framework import serializers
from books.models import Book


class GetBookSerializer(serializers.ModelSerializer):
    book_type_text = serializers.SerializerMethodField(
        method_name='get_book_type_text',
        read_only=True
    )

    def get_book_type_text(self, instance):
        return instance.get_book_type_display()

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'book_type_text']


class PostBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'title': {'write_only': True},
            'price': {'write_only': True},
            'book_type': {'write_only': True},
        }


class FullBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
