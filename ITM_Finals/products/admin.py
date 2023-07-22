from django.contrib import admin

from .models import Category, Product
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'product_name', 'price', 'available')
    list_editable=('available',)
admin.site.register(Product, ProductAdmin)
