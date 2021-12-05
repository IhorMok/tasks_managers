from rest_framework import serializers

from task.tags.models import Tag


class SimplifiedTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "update", "creation"]

