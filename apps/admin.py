from django.contrib import admin
from apps.models import Product, Tag, ProductImage



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'short_description', 'price', 'is_premium', 'description', 'shopping_cost', 'specification',
        'discount', 'quantity')

    fields = (
        'name', 'short_description', 'price', 'is_premium', 'description', 'shopping_cost', 'specification', 'tags',
        'author ',
        'discount', 'quantity')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    fields = ('product', 'image')
