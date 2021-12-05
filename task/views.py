import django_filters
from django.shortcuts import render
from django.http import HttpResponse, request

from rest_framework import viewsets, permissions, generics

from .tags.models import Tag
from .tags.serializers.serializer import TagSerializer
from .tasks.models import Task
from .tasks.serializers.serializers import TaskSerializer


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

