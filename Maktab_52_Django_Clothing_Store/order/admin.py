from django.contrib import admin

# Register your models here.
from order.models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'payment_type', 'is_deleted']
    list_editable = ['is_deleted']
    search_fields = ['user__phone', 'status', 'payment_type']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'is_deleted', 'total_price_of_item']
    list_editable = ['is_deleted']
    list_display_links = ['order']
    search_fields = ['product__name']
