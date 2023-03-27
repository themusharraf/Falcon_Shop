from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from django.contrib.admin.options import InlineModelAdmin
from django.utils.html import format_html
from apps.models import Product, Tag, ProductImage


class ProductImagesInline(StackedInline):
    min_num = 1
    extra = 0
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImagesInline,)
    list_display = (
        'title', 'short_description', 'price', 'is_premium', 'shopping_cost', 'specification',
        'discount', 'quantity')

    fields = (
        'title', 'short_description', 'price', 'is_premium', 'description', 'shopping_cost', 'specification', 'tags',
        'author',
        'discount', 'quantity')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_tag')

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted.objects:
            obj.delete()
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save.m2m()
