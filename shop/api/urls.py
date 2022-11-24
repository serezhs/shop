from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryDetail,
    CategoryList,
    ProductViewSet,
    APICart,
    CartList,
)

router = routers.DefaultRouter()

router.register("products", ProductViewSet)

urlpatterns = [
    path("cart/", CartList.as_view()),
    path("products/<int:id>/cart/", APICart.as_view()),
    path("categories/", CategoryList.as_view()),
    path("categories/<slug:slug>/", CategoryDetail.as_view()),
    path("", include(router.urls)),
]
