from django.contrib import admin

# Register your models here.
from product.models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Discount)
