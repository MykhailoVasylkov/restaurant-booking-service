from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation
from datetime import datetime, timedelta


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

            # Get the date and time of new booking
            new_reservation_date = reservation.date
            new_reservation_time = reservation.time

            # Determine the time range (20 minutes before and after)
            time_range_start = (datetime.combine(new_reservation_date, new_reservation_time) - timedelta(minutes=20)).time()
            time_range_end = (datetime.combine(new_reservation_date, new_reservation_time) + timedelta(minutes=20)).time()

            # We check if there is a booking on the same day and in this range
            conflicting_reservation = Reservation.objects.filter(
                date=new_reservation_date,
                time__gte=time_range_start,
                time__lte=time_range_end
            )

            if conflicting_reservation.exists():
                messages.add_message(request, messages.WARNING, 'You already have a reservation for this time. Please edit the existing reservation to make changes.')
                return redirect('booking')

            # If there are no intersections, we save booking
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
