from rest_framework import generics, permissions
from accounts.models import Account
from accounts.serializers import AccountSerializer
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

    # if doen't specify this, other user will see everyone's infor is go to detail accounts/1
    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsOwner
    ]