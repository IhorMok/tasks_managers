from task.tags.models import Tag
from task.tags.serializers.simplified_serializer import SimplifiedTagSerializer


class TagSerializer(SimplifiedTagSerializer):
    from task.tasks.serializers.simplified_serializer import SimplifiedTaskSerializer
    tasks = SimplifiedTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ["id", "name", "update", "creation", "tasks"]
