from django.http import HttpResponse
from django.shortcuts import render

from online_store.models import Product


def home(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "home.html", context)


def category_1(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "category_1.html", context)


def catalog(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "catalog.html", context)


def contact_feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо {name}! Сообщение получено.")
    return render(request, "contact.html")
