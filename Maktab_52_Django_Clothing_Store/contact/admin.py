from django.contrib import admin

# Register your models here.
from contact.models import *


@admin.register(Contact)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
