from django.contrib import admin
from .models import Product, Sale, Ingredient, Consumables, CheckList


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity',
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


class CheckListAdmin(admin.ModelAdmin):
    list_display = (
        'check_time',
        'seller',
        'summary_price',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Consumables)
admin.site.register(CheckList, CheckListAdmin)
