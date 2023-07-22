from django.contrib import admin

from .models import *

admin.site.register(Customer)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id', 'customer', 'date_ordered', 'complete',)
    list_editable=('complete',)
admin.site.register(Order, OrderAdmin)

admin.site.register(OrderItem)
admin.site.register(ShippingAddress)