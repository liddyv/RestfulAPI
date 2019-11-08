from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.utils.http import urlencode
from cards.views import CardList
from cards.models import Card


class GetCardsTest(APITestCase):
    def setUp(self):
        cards = [
            ("MyCard1", "My card1 description", "to-do"),
            ("MyCard2", "My card2 description", "in-progress"),
            ("MyCard3", "My card3 description", "done")
        ]
        for card in cards:
            Card.objects.create(
                title=card[0],
                description=card[1],
                status=card[2]
            )

    def test_get_all_accounts(self):
        url = reverse(CardList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_get_cards_by_status(self):
        url = reverse(CardList.name)
        url = '{}?{}'.format(
            url,
            urlencode({'search': 'to-do'})
        )
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['title'] == 'MyCard1'

    def test_get_cards_ordered_by_title(self):
        url = reverse(CardList.name)
        url = '{}?{}'.format(
            url,
            urlencode({'ordering': '-title'})
        )
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3
        assert response.data[0]['title'] == 'MyCard3'
