from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from online_store.forms import ProductForm
from online_store.models import Category, Product
from online_store.services import get_product_from_cache


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_product_from_cache()


class ProductCatalogListView(ListView):
    model = Product
    template_name = "online_store/products.html"
    context_object_name = "object_list"

    def get_queryset(self):
        # Если пользователь имеет права модератора, показываем все товары
        if self.request.user.has_perm("online_store.can_delete_product"):
            return Product.objects.all()
        # Иначе показываем только опубликованные товары
        return Product.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаем информацию о правах пользователя в шаблон
        context["can_delete"] = self.request.user.has_perm(
            "online_store.can_delete_product"
        )
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("online_store:products")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["can_delete"] = user.has_perm("online_store.delete_product")
        context["can_change"] = user.has_perm("online_store.change_product")
        return context


class ContactFeedbackView(View):
    def get(self, request):
        # Отображаем форму
        return render(request, "online_store/contact.html")

    def post(self, request):
        # Обработка отправки формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо {name}! Сообщение получено.")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy(
        "online_store:products"
    )  # Переадресация на список постов после удаления
    template_name = "online_store/product_list.html"


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "online_store/product_edit.html"

    def get_success_url(self):
        # Переадресация на страницу деталей после успешного редактирования
        return reverse_lazy(
            "online_store:product_detail", kwargs={"pk": self.object.pk}
        )


class CategoryProductsView(ListView):
    """Отображение списка всех категорий."""

    model = Category
    template_name = "online_store/category_list.html"


class CategoryDetailView(ListView):
    """Представление для отображения списка продуктов в указанной категории."""

    model = Product
    template_name = "online_store/category_detail.html"
    context_object_name = "products"

    def get_queryset(self):
        """Возвращает список продуктов в указанной категории."""
        category_name = self.kwargs["category_name"]  # Получаем имя категории из URL
        category = get_object_or_404(Category, name=category_name)  # Находим категорию
        return Product.objects.filter(
            category=category
        )  # Фильтруем товары по категории

    def get_context_data(self, **kwargs):
        """Добавляем категорию в контекст шаблона."""
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(
            Category, name=self.kwargs["category_name"]
        )
        return context
