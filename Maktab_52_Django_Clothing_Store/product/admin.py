from django.contrib import admin

# Register your models here.
from product.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_deleted']
    list_editable = ['price', 'is_deleted']
    search_fields = ['name', 'price', 'category__name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'is_deleted']
    list_editable = ['parent', 'is_deleted']
    search_fields = ['name', 'parent']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_deleted']
    list_editable = ['is_deleted']
    search_fields = ['name']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'type', 'is_deleted']
    list_editable = ['amount', 'type', 'is_deleted']
    search_fields = ['name', 'amount', 'type']
