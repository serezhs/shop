from rest_framework import routers

from django.urls import include, path

from .views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
