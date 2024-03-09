from django.shortcuts import render

# Create your views here.

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Home - каталог",
        "goods": goods
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)
