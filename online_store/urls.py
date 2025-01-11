from django.urls import path

from online_store.apps import OnlineStoreConfig

from online_store.views import home, contact, catalog, category_1

app_name = OnlineStoreConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("", contact, name="contact"),
    path("", catalog, name="catalog"),
    path("", category_1, name="category_1"),
]
