from django.db import models
from task.models import Base


class Task(Base):
    class Priority(models.TextChoices):
        low = 'Low'
        medium = 'Medium'
        high = 'High'

    class Status(models.TextChoices):
        backlog = "Backlog"
        in_progress = 'In Progress'
        done = 'Done'

    title = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.medium)
    status = models.CharField(max_length=15, default=Status.backlog)
    tags = models.ManyToManyField('task.Tag', related_name="tasks", db_table="task_tag_tasks")
