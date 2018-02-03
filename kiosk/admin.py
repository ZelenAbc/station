from django.contrib import admin
from .models import Product, Sale, Ingredient, Consumables

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Ingredient)
admin.site.register(Consumables)
