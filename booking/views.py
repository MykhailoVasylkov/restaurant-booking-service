from django.shortcuts import render
from django.views import generic

# Create your views here.

def booking_page(request):
    return render(request, 'booking/booking_page.html')