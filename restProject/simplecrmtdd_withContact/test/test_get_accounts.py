from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.utils.http import urlencode
from accounts.views import AccountList
from accounts.models import Account


class GetAccountsTest(APITestCase):
    def setUp(self):
        accounts = [
            ("Bank of America", "Banking"),
            ("UCSC Extension", "Education")
        ]
        for account in accounts:
            Account.objects.create(
                name=account[0],
                industry=account[1]
            )

    def test_get_all_accounts(self):
        url = reverse(AccountList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_get_accounts_by_industry(self):
        url = reverse(AccountList.name)
        url = '{}?{}'.format(
            url,
            urlencode({'search': 'Banking'})
        )
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['name'] == 'Bank of America'

    def test_get_accounts_ordered_by_name(self):
        url = reverse(AccountList.name)
        url = '{}?{}'.format(
            url,
            urlencode({'ordering': '-name'})
        )
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['name'] == 'UCSC Extension'
