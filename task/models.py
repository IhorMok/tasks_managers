from django.db import models


class Base(models.Model):
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
