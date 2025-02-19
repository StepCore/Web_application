from django.forms import ModelForm

from online_store.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
