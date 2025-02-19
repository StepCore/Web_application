from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, View

from online_store.models import Product


class ProductListView(ListView):
    model = Product


class ProductCatalogListView(ListView):
    model = Product
    template_name = "online_store/products.html"


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("online_store:products")


class ProductDetailView(DetailView):
    model = Product


class ContactFeedbackView(View):
    def get(self, request):
        # Отображаем форму
        return render(request, "online_store/contact.html")

    def post(self, request):
        # Обработка отправки формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо {name}! Сообщение получено.")
