from django.db import models
from task.models import Base


class Tag(Base):
    name = models.TextField(max_length=128)
