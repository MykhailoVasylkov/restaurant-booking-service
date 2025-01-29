from django.shortcuts import render, redirect, get_list_or_404
from django.views import generic
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation


# Create your views here.

def booking_page(request):
    # Фильтруем бронирования только текущего пользователя
    queryset = Reservation.objects.filter(client=request.user).order_by("-created_at")

    # Если у пользователя нет бронирований, get_list_or_404 вызовет 404, поэтому лучше использовать просто QuerySet
    booking_list = queryset if queryset.exists() else []

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Привязываем бронирование к пользователю
            reservation.save()
            messages.success(request, 'Reservation submitted and awaiting approval')
    else:
        form = ReservationForm()
    
    return render(request, 'booking/booking_page.html', {
        'form': form,
        'booking_list': booking_list,  # Передаем бронирования в шаблон
    })
