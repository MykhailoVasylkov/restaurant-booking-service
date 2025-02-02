from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name='booking'),
    path('edit/<int:pk>', views.edit_booking, name='edit_booking'),
]