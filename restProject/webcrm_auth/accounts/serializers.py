from rest_framework import serializers
from accounts.models import Account, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(
        many=True, read_only=True
    )

    owner = serializers.ReadOnlyField(
        source='owner.username'
    )

    class Meta:
        model = Account
        fields = '__all__'
