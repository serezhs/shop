from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    search_fields = ("name", "price")
    list_filter = ("available", "category")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
