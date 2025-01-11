from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def category_1(request):
    return render(request, "category_1.html")


def catalog(request):
    return render(request, "catalog.html")


def contact_feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо {name}! Сообщение получено.")
    return render(request, 'contact.html')
