from django.contrib import admin

from .models import Category, Product, Cart


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    search_fields = ("name", "price")
    list_filter = ("available", "category")


class CartAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "user")
    search_fields = ("user__email", "product__name")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
