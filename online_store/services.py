from django.core.cache import cache

from config.settings import CACHED_ENABLED
from online_store.models import Category, Product


def get_product_from_cache():
    """Получение данных о продуктах из кэша"""
    if not CACHED_ENABLED:
        return Product.objects.all()
    key = "product_list"
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product
