from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from task.tasks.models import Task


class SimplifiedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", 'title', 'description', 'creation', 'priority',
                  'status', 'update']
