from django.contrib import admin
from content.models import *
# Register your models here

@admin.register(Item, Category, Cart, Mobile, Refrigerator, laptop, WashingMachine)
class ShoppingAdmin(admin.ModelAdmin):
    readonly_fields = ('updated_date', 'created_date')

@admin.register(CartDetailThrough)
class CartDetailThroughAdmin(admin.ModelAdmin):
    readonly_fields = ('cart', 'item', 'quantity', 'color', 'state')