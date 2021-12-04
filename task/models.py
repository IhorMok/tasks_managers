from django.db import models


class Base(models.Model):
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Tag(Base):
    name = models.TextField(max_length=128)


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
    tags = models.ManyToManyField(Tag)
