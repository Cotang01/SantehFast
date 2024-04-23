from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['phone', 'full_name', 'address', 'status']
    list_filter = ['address', 'status']


admin.site.register(Order, OrderAdmin)
