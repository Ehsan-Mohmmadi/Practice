from django.shortcuts import render

from product_module.models import Product


def product_list(request):
    return render(request, 'product_module/product_list.html', context={'products': Product.objects.all()})