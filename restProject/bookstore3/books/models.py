from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Book(models.Model):
    TYPE_KINDLE = 'kindle'
    TYPE_PAPERBACK = 'paperback'
    TYPE_HARDCOVER = 'hardcover'
    TYPE_CHOICES = (
        (TYPE_KINDLE, 'kindle'),
        (TYPE_PAPERBACK, 'paperback'),
        (TYPE_HARDCOVER, 'hardcover'),
    )

    title = models.CharField(max_length=50, unique=True)
    # max_length checking is in serializer level v.s. unique is at db level
    price = models.FloatField(default=0)
    description = models.CharField(blank=True, max_length=250)
    book_type = models.CharField(
        max_length=250,
        choices=TYPE_CHOICES, #choices is checked in serializer level
        default=TYPE_PAPERBACK)

    def __str__(self):
        return '{}: {} ({})'.format(
            self.id,
            self.title,
            self.get_book_type_display() #.get_<COLUMN_NAME>_display() method is auto-generated
        )


class Comment(models.Model):
    content = models.CharField(max_length=250)
    # e.g., 2019-07-04
    comment_date = models.DateField()
    comment_user = models.CharField(max_length=50, blank=True)
    #book_id = 1
    book = models.ForeignKey(
        Book,
        related_name='cmts',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )


class Rating(models.Model):
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    book = models.ForeignKey(
        Book,
        related_name='ratings',
        on_delete=models.CASCADE
    )