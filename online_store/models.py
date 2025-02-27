from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название товара")
    description = models.CharField(max_length=150, verbose_name="Описание товара")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение товара")
    category = models.CharField(max_length=150, verbose_name="Категория товара")
    price = models.CharField(max_length=150, verbose_name="Цена товара")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания товара"
    )
    updated_at = models.DateField(
        auto_now_add=True, verbose_name="Дата последнего изменения товара"
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца товара",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")
    description = models.CharField(max_length=150, verbose_name="Описание категории")
