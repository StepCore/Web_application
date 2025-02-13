from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("online_store.urls", namespace="online_store")),
    path("blogs/", include("blog_app.urls", namespace="blog_app")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
