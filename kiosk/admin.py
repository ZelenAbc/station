from django.contrib import admin
from .models import Product, Sale, Provider, Ingredient, FiscalCheck

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Provider)
admin.site.register(Ingredient)
admin.site.register(FiscalCheck)
