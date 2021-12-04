from .models import Tag, Task
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "update"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", 'title', 'description', 'creation', 'priority',
                  'status', 'update', 'tags']




