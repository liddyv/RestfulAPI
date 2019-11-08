from django.urls import reverse
from django.utils.http import urlencode
from cards.views import CardList, TaskList


def post_task(client, card_id, description, done):
    url = reverse(TaskList.name)
    response = client.post(
        url,
        {
            'card': card_id,
            'description': description,
            'done': done
        },
        format='json'
    )
    return response


def post_card(client, title, description, status):
    url = reverse(CardList.name)
    response = client.post(
        url,
        {
            'title': title,
            'description': description,
            'status': status
        },
        format='json'
    )
    return response