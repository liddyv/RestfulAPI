from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.views import AccountList

class GetAccountsTest(APITestCase):
    def setUp(self): #this will be executed before other methods
        accounts = [("Bank of America", "banking"),
                    ("UCSC Extension", "Education")]
        for account in accounts:
            Account.objects.create(
                name = account[0],
                industry = account[1]
            )

    def test_get_all_accounts(self):
        url = reverse(AccountList.name)
        response = self.client.get(url, format='json') #a client to similate browser
        assert response.status.code == status.HTTP_200_OK
        assert len(response.data) == 2