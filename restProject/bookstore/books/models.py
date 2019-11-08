from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return '{}: {} ${}'.format(
            self.id, self.title, self.price
        )
