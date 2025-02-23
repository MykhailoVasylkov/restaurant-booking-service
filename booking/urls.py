from django.urls import path
from . import views

"""
URL patterns for booking:
1. Booking page, 2. Edit booking, 3. Delete booking.
"""


urlpatterns = [
    path('', views.booking_page, name='booking'),
    path('edit/<int:pk>', views.edit_booking, name='edit_booking'),
    path('delete/<int:pk>', views.delete_booking, name='delete_booking'),
]
