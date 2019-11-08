'''
Testing the following test cases:
1. Creating a Kanban card anonymously receives 401 status;
2. Creating a Kanban card with valid username and password will receive 201
status;
3. Creating a task for an existing Kanban card with valid username and
password.
'''

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from cards.views import CardList
import utils

class PostCardTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='mary',
            password='mary123'
        )
    #1. Creating a Kanban card anonymously receives 401 status;
    def test_post_card_anonymously(self):
        response = utils.post_card(
            self.client, 'HappyCard1', 'HappyCard1 Description', 'done'
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    #2. Creating a Kanban card with valid username and password will receive 201 status;
    def test_post_card(self):
        self.client.force_authenticate(
            user=self.user
        )
        response = utils.post_card(
            self.client, 'HappyCard1', 'HappyCard1 Description', 'done'
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'HappyCard1'

    def test_post_same_card_twice(self):
        self.client.force_authenticate(
            user=self.user
        )
        utils.post_card(
            self.client, 'HappyCard1', 'HappyCard1 Description', 'done'
        )
        response = utils.post_card(
            self.client, 'HappyCard1', 'HappyCard1 Description', 'done'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    #3. Creating a task for an existing Kanban card with valid username and password.
    def test_post_card_then_task(self):
        self.client.force_authenticate(
            user=self.user
        )
        response = utils.post_card(
            self.client, 'HappyCard2', 'HappyCard2 Description', 'in-progress'
        )
        card_id = response.data['id']
        response = utils.post_task(
            self.client, card_id, 'task1-be happy', True
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['description'] == 'task1-be happy'

        card_id = response.data['id']
        response = utils.post_task(
            self.client, card_id, 'task2-be healthy', True
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['description'] == 'task2-be healthy'

        url = reverse(CardList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'tasks' in response.data[0]
        assert len(response.data[0]['tasks']) == 2
        assert response.data[0]['tasks'][0]['description'] == 'task1-be happy'
        assert response.data[0]['tasks'][1]['description'] == 'task2-be healthy'

