from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    book_type = models.CharField(
        max_length=10,
        choices=(
            ('KD', 'Kinder'),
            ('PR', 'Paperback'),
            ('HD', 'Hardcover')
        ),
        default='PR'
    )
