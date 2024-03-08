from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page":  "Текст о том что магазин хороший и товар отличный"
        }
    return render(request, "main/about.html", context)

def ship(request):
    context = {
        'title': 'Доставка и оплата',
        'content': 'Доставка быстрая как и ваша оплата',
        'text_on_page': 'Что типо про доставку и тд'
    }
    return render(request, "main/ship.html", context)


def contact(request):
    context = {
        "title": "Контактная информация",
        "content": "Контактная информация",
        "text_on_page": "Наша почта - test@test.com",
        "text_on_page_two": "Номер Тех-Поддержки 8-(800)-55-35"
    }
    return render(request, "main/contact.html", context)
