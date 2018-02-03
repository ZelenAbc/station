from django.db import models
from django.contrib.auth.models import User


# from django.utils import timezone


class Product(models.Model):  # products that has a button in tha application
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Consumables(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    consumables = models.ForeignKey(Consumables, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.consumables

    def get_available_number(self):
        consumables_quantity = self.consumables.quantity
        available_number = consumables_quantity / self.quantity
        return available_number


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.SmallIntegerField(default=0, null=False)

    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    check_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.product, self.quantity)
