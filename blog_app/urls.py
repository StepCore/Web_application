from django.urls import path

from .views import (BlogPostCreateView, BlogPostDeleteView, BlogPostDetailView,
                    BlogPostListView, BlogPostUpdateView)

app_name = "blog"

urlpatterns = [
    path("create/", BlogPostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", BlogPostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogPostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="post_delete"),
    path("", BlogPostListView.as_view(), name="post_list"),
]
