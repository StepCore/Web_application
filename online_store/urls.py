from django.urls import path

from online_store.apps import OnlineStoreConfig
from online_store.views import catalog, category_1, contact_feedback, home

app_name = OnlineStoreConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact_feedback, name="contact"),
    path("catalog/", catalog, name="catalog"),
    path("category_1/", category_1, name="category_1"),
]
