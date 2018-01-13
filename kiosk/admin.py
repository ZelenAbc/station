from django.contrib import admin
from .models import Product, Sale, Provider, Ingredient, FiscalCheck, Consumables, Offer

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Provider)
admin.site.register(Ingredient)
admin.site.register(FiscalCheck)
admin.site.register(Consumables)
admin.site.register(Offer)
