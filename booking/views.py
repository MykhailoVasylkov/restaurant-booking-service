from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def booking_page(request):
    return render(request, 'booking/booking_page.html')