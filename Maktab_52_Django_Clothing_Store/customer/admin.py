from django.contrib import admin

# Register your models here.
from customer.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone', 'first_name', 'last_name', 'username']
    list_editable = ['username']
    list_display_links = ['phone']
    search_fields = ['phone', 'username']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['owner', 'city', 'province']
    list_display_links = ['owner']
    search_fields = ['owner__phone', 'owner__username', 'city']
