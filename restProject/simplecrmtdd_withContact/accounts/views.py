from rest_framework import generics, permissions
from accounts.models import Account, Contact
from accounts.serializers import AccountSerializer, ContactSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    name = 'account-list'
    search_fields = ('industry',)
    ordering_fields = ('name', )

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class ContactList(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    name = 'contact-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

