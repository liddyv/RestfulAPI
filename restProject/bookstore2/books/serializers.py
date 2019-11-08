from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=250)
    price = serializers.FloatField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            'title', instance.title
        )
        instance.price = validated_data.get(
            'price', instance.price
        )
        instance.save()
        return instance

