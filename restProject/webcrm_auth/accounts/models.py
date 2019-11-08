from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=100, unique=True)
    industry = models.CharField(max_length=50)

    owner = models.ForeignKey(
        'auth.User',
        related_name='accounts',
        on_delete=models.CASCADE
    )


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    account = models.ForeignKey(
        Account,
        related_name='contacts',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('account', 'name')
