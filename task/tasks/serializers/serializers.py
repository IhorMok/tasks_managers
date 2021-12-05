from task.tasks.models import Task
from task.tasks.serializers.simplified_serializer import SimplifiedTaskSerializer


class TaskSerializer(SimplifiedTaskSerializer):
    from task.tags.serializers.serializer import SimplifiedTagSerializer
    tags = SimplifiedTagSerializer(many=True, read_only=False)

    class Meta:
        model = Task
        fields = ["id", 'title', 'description', 'creation', 'priority',
                  'status', 'update', "tags"]

    def update(self, instance, validated_data):
        # Todo: find tags by ids, validate priority uniqueness.
        return Task.objects.update(**validated_data)