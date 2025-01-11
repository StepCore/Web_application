from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def category_1(request):
    return render(request, "category_1.html")


def catalog(request):
    return render(request, "catalog.html")
