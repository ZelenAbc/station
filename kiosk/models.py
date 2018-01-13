from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Provider(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Consumables(models.Model):
    name = models.CharField(max_length=200)
    size = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Offer(models.Model):
    consumables = models.ForeignKey(Consumables, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=False)
    cost = models.FloatField(default=0)
    is_actual = models.BooleanField(default=True)


class Product(models.Model):  # products that has a button in tha application
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_cost_price(self):
        return self.name


class Ingredient(models.Model):
    consumables = models.ForeignKey(Consumables, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.consumables)


class FiscalCheck(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    check_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.seller) + " " + str(self.check_time)


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    count = models.SmallIntegerField(default=0, null=False)

    fiscal_check = models.ForeignKey(FiscalCheck, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product) + " " + str(self.count)

