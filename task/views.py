import django_filters
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Tag, Task
from rest_framework import viewsets, permissions, generics
from .serializers import TagSerializer, TaskSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']

class TaskViewsSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['priority', 'status']






# def index(request):
#     return HttpResponse("Test pages!")

