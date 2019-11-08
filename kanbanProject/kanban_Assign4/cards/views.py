from rest_framework import generics, permissions
from cards.models import Card, Task
from cards.serializers import CardSerializer, TaskSerializer
from django.core import exceptions


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    name = 'card-list'
    search_fields = ('status', )
    ordering_fields = ('title', )

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    name = 'card-detail'

    permission_classes = (
        permissions.IsAuthenticated,
    )


#class TaskList(generics.ListCreateAPIView):
class TaskList(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'task-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'task-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
