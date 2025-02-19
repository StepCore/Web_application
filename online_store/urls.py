from django.urls import path

from online_store.apps import OnlineStoreConfig
from online_store.views import (ContactFeedbackView, ProductCatalogListView,
                                ProductDetailView, ProductListView)

app_name = OnlineStoreConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contact/", ContactFeedbackView.as_view(), name="contact"),
    path("products/", ProductCatalogListView.as_view(), name="products"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
]
