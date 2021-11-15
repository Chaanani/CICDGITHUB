from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo, TodoList
from todo.serializers import TodoSerializer, TodoListSerializer, TodoListDetailSerializer


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['due_date', 'favourite', 'completed']
    search_fields = ['title']

    @swagger_auto_schema(operation_description="This method returns a list of Todos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TodoListDetailSerializer
        return TodoListSerializer
