from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название"
    )
    slug = models.SlugField(unique=True, verbose_name="Слаг")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        blank=True,
        null=True,
        verbose_name="Категория",
    )
    image = models.ImageField(
        upload_to="products/images/",
        null=True,
        default=None,
        verbose_name="Фото",
    )
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], verbose_name="Цена"
    )
    available = models.BooleanField(default=False, verbose_name="В наличии")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="shopping_cart",
        verbose_name="Товар",
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество", default=1
    )

    class Meta:
        unique_together = ("user", "product")
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return self.product, self.quantity, self.user
