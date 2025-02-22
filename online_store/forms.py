from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "description", "price", "image"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для полей
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название товара"}
        )

        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите категорию товара"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание товара"}
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите цену товара"}
        )

        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if not price.isdigit() or int(price) <= 0:
            raise ValidationError(
                "Пожалуйста укажите целое положительное число не равное 0"
            )
        return int(price)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        if name and any(word in name.lower() for word in forbidden_words):
            self.add_error("name", "Используется запрещенное слово")
        if description and any(word in description.lower() for word in forbidden_words):
            self.add_error("description", "Используется запрещенное слово")

    def clean_image(self):
        image = self.cleaned_data.get("image")

        if image:
            # Проверка формата файла
            allowed_formats = ["image/jpeg", "image/png"]
            if image.content_type not in allowed_formats:
                raise ValidationError("Допустимые форматы изображений: JPEG и PNG.")

            # Проверка размера файла (5 МБ = 5 * 1024 * 1024 байт)
            max_size = 5 * 1024 * 1024  # 5 МБ
            if image.size > max_size:
                raise ValidationError("Максимальный размер файла: 5 МБ.")

        return image
