# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal
from .models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class productAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',
        'price',
        'rating',
        'category',
        'image',
        'image_url',
    ) 

    ordering = ('category', 'brand')


admin.site.register(Product)
admin.site.register(Category)
