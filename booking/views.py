from django.shortcuts import render, redirect, get_list_or_404
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from .forms import ReservationForm
from .models import Reservation


# Create your views here.

def booking_page(request):
    now = timezone.now()
    if request.user.is_authenticated:
        queryset = Reservation.objects.filter(client=request.user).order_by("created_at")
        booking_list = queryset if queryset.exists() else []
    else:
        booking_list = []

    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(request, messages.SUCCESS, 'Reservation submitted and awaiting approval')
            return redirect('booking')
        else:
            messages.add_message(request, messages.WARNING, 'Please log in to make a reservation.')
            return redirect('booking')

    form = ReservationForm()
    
    
    return render(request, 'booking/booking_page.html', {
        'form': form,
        'booking_list': booking_list,
        'now': now,
    })
