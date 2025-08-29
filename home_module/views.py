from django.shortcuts import render


def header_component(request):
    return render(request,'shared/header_component.html')
def home(request):
    return render(request,'shared/_layout.html')