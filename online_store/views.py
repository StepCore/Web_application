from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from online_store.models import Product


class ProductListView(ListView):
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


def products(request):
    products_list = Product.objects.all()
    context = {
        "products_list": products_list,
    }
    return render(request, "online_store/products.html", context)


def catalog(request):
    products_list = Product.objects.all()
    context = {
        "products_list": products_list,
    }
    return render(request, "online_store/catalog.html", context)