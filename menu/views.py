from django.shortcuts import render
from django.views import generic

# Create your views here.

def menu_page(request):
    return render(request, 'menu/menu_page.html')