from rest_framework import generics, permissions
from django.core import exceptions
from accounts.models import Account, Contact
from accounts.serializers import AccountSerializer, ContactSerializer
from accounts.utils import custom_permissions


class AccountList(generics.ListCreateAPIView):
    serializer_class = AccountSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Account.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsOwner
    ]


class ContactList(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        if serializer.validated_data['account'].owner != self.request.user:
            raise exceptions.PermissionDenied
        else:
            serializer.save()

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsAccountOwner
    ]