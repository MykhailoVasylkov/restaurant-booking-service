from django.shortcuts import render
from django.views import generic

"""Render the home page."""


def home_page(request):
    return render(request, 'home/index.html')
