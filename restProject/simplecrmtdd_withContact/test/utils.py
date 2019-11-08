from django.urls import reverse
from django.utils.http import urlencode
from accounts.views import AccountList, ContactList


def post_contact(client, account_id, name, phone):
    url = reverse(ContactList.name)
    response = client.post(
        url,
        {
            'account': account_id,
            'name': name,
            'phone': phone
        },
        format='json'
    )
    return response


def post_account(client, name, industry):
    url = reverse(AccountList.name)
    response = client.post(
        url,
        {
            'name': name,
            'industry': industry
        },
        format='json'
    )
    return response