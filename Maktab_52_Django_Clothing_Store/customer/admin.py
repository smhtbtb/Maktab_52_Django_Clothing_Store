from django.contrib import admin

# Register your models here.
from customer.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone', 'first_name', 'last_name', 'is_active']
    list_display_links = ['phone']
    list_editable = ['is_active']
    search_fields = ['phone']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['owner', 'city', 'province']
    list_display_links = ['owner']
    search_fields = ['owner__phone', 'owner__username', 'city']
