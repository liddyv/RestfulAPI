from rest_framework import generics, permissions
from cards.models import Card, Task
from cards.serializers import CardSerializer, TaskSerializer
from django.core import exceptions
from cards.utils import custom_permissions


class CardList(generics.ListCreateAPIView):
    '''
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    name = 'card-list'
    '''
    serializer_class = CardSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]
    #Try this
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Card.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    name = 'card-detail'
    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsOwner
    ]


class TaskList(generics.ListCreateAPIView):
#class TaskList(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'task-list'

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        if serializer.validated_data['card'].owner != self.request.user:
            raise exceptions.PermissionDenied
        else:
            serializer.save()


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'task-detail'

    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsCardOwner
    ]