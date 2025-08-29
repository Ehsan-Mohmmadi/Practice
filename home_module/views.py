from django.shortcuts import render

def home(request):
    render(request,'shared/_layout.html')