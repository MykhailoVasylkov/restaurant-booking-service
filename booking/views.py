from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation


# Create your views here.

def booking_page(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Reservation submitted and awaiting approval'
                )
    else:
        form = ReservationForm()
    
    return render(request, 'booking/booking_page.html', {'form': form})
    
