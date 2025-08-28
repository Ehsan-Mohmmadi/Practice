from django.shortcuts import render
from django.views.generic import ListView


class ProductView(ListView):
    template_name = ''