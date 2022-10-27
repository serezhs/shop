from rest_framework import routers

from django.urls import include, path

from .views import CategoryViewSet, ProductViewSet, APICategory

router = routers.DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)

urlpatterns = [
    path("categories/<slug:slug>/", APICategory.as_view()),
    path("", include(router.urls)),
]
