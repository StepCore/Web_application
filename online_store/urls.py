from django.urls import path

from online_store.apps import OnlineStoreConfig
from online_store.views import (ContactFeedbackView, ProductCatalogListView,
                                ProductCreateView, ProductDeleteView,
                                ProductDetailView, ProductListView,
                                ProductUpdateView)

app_name = OnlineStoreConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contact/", ContactFeedbackView.as_view(), name="contact"),
    path("products/", ProductCatalogListView.as_view(), name="products"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
]
