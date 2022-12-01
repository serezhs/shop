from django.shortcuts import get_object_or_404
from products.models import Cart, Category, Product
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters

from .serializers import (
    CategoryDetailSerializer,
    CategorySerializer,
    ProductDetailSerializer,
    CartSerializer,
)
from .pagination import ProductPagination
from .permissions import IsAdminOrReadOnly


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = "slug"
    permission_classes = (IsAdminOrReadOnly,)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    pagination_class = ProductPagination
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ("name", "category__name")
    ordering_fields = ("price",)
    ordering = ("-available",)
    permission_classes = (IsAdminOrReadOnly,)


class CartList(generics.ListAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user

        queryset = Cart.objects.filter(user=user)
        return queryset


class APICart(APIView):
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)

        if product.available is False:
            return Response(
                {
                    "errors": (
                        "Извините, в данный момент "
                        "товар не доступен к покупке"
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user
        cart = Cart.objects.filter(user=user, product=product)

        if cart.exists():
            cart = Cart.objects.get(user=user, product=product)
            cart.quantity += 1
            cart.save()

            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            cart = Cart.objects.create(user=user, product=product)

            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        user = request.user
        cart = Cart.objects.filter(user=user, product=product)

        if cart.exists():
            cart = Cart.objects.get(user=user, product=product)

            if cart.quantity > 1:
                cart.quantity -= 1
                cart.save()

            else:
                cart.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            {"errors": "Этого товара уже нет в корзине"},
            status=status.HTTP_400_BAD_REQUEST,
        )
