from django.urls import path

from online_store.apps import OnlineStoreConfig
from online_store.views import catalog, products, ContactFeedbackView, ProductListView

app_name = OnlineStoreConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contact/", ContactFeedbackView.as_view(), name="contact"),
    path("catalog/", catalog, name="catalog"),
    path("products/", products, name="products"),
]
