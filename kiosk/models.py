from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
