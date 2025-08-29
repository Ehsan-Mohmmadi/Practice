from django.shortcuts import render
from django.views.generic import DetailView

from product_module.models import Product


def product_list(request):
    return render(request, 'product_module/product_list.html', context={'products': Product.objects.all()})

class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context