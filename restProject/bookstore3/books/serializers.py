from rest_framework import serializers
from django.db.models import Avg
from books.models import Book, Comment, Rating


class BookSerializer(serializers.ModelSerializer):
    '''
    cmts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )
    '''


    cmts = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
        )


    '''
    ratings = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='rating'
    )
    '''

    popular = serializers.SerializerMethodField(
        method_name='is_popular', read_only=True
    )

    def is_popular(selfself, instance):
        result = Rating.objects.filter(book=instance.pk).aggregate(Avg('rating'))
        avg = result['rating__avg']
        return avg is not None and avg >=3


    class Meta:
        model = Book
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rating
        fields = '__all__'