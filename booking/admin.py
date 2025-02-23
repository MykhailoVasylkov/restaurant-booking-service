from django.contrib import admin
from .models import Reservation

"""
Register Reservation model in admin panel.
Add how reservations are displaying.
Add search functionality.
Add filter functionality.
"""


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'client',
        'phone_number',
        'date',
        'time',
        'table_count',
        'status'
        )
    search_fields = ['client', 'phone_number', 'comment']
    list_filter = ('date', 'status')
