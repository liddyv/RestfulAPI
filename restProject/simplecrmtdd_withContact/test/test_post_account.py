from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.views import AccountList
import utils

class PostAccountTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='john',
            password='johnpwd'
        )

    def test_post_account_anonymously(self):
        response = utils.post_account(
            self.client, 'Apple', 'High Tech'
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_post_account(self):
        self.client.force_authenticate(
            user=self.user
        )
        response = utils.post_account(
            self.client, 'Apple', 'High Tech'
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == 'Apple'

    def test_post_same_account_twice(self):
        self.client.force_authenticate(
            user=self.user
        )
        utils.post_account(
            self.client, 'Apple', 'High Tech'
        )
        response = utils.post_account(
            self.client, 'Apple', 'High Tech'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_account_then_contact(self):
        self.client.force_authenticate(
            user=self.user
        )
        response = utils.post_account(
            self.client, 'Apple', 'High Tech'
        )
        account_id = response.data['id']
        response = utils.post_contact(
            self.client, account_id, 'Alice', '415-111-2222'
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == 'Alice'

        url = reverse(AccountList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'contacts' in response.data[0]
        assert len(response.data[0]['contacts']) == 1
        assert response.data[0]['contacts'][0]['name'] == 'Alice'

