from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from products.models import Category, Product, Cart


class ProductSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "image",
            "price",
            "available",
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "category",
            "image",
            "price",
            "available",
        )


class MiniProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ("name", "products")
        lookup_field = "slug"


class CartSerializer(serializers.ModelSerializer):
    product = MiniProductSerializer(read_only=True)
    common_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = (
            "product",
            "quantity",
            "common_price",
        )

    def get_common_price(self, obj):
        return obj.quantity * obj.product.price
