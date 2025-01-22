from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def menu_page(request):
    return render(request, 'menu/menu_page.html')