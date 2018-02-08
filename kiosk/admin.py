from django.contrib import admin
from .models import Product, Sale, Ingredient, Consumables


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity',
        'seller',
        'check_time',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost',
    )


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'consumables',
        'quantity',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Consumables)
