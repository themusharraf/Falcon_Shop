from django.contrib import admin
from apps.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'description','long_description','discount','number','shop_cost','tags'
                    ,'specification')
    fields = ('name', 'image', 'price', 'description')