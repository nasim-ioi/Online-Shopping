from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Order)
class FinanceAdmin(admin.ModelAdmin):
    readonly_fields = ('customer_username', 'address', 'province', 
    'city', 'phone', 'item_title', 'item_id', 'color', 'quantity', 'baught_date')