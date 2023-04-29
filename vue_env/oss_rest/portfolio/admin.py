from django.contrib import admin
from .models import Customer, Inventory, Order

class CustomerList(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    # search_fields = ( 'name')
    # ordering = ['name']


class InventoryList(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'price')
    list_filter = ('name',)
    # search_fields = ('name')
    # ordering = ['name']


class OrderList(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'total_price')
    list_filter = ('customer',)
    # search_fields = ('customer')
    # ordering = ['customer']


admin.site.register(Customer, CustomerList)
admin.site.register(Inventory, InventoryList)
admin.site.register(Order, OrderList)
