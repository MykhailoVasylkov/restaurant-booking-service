"""
    URL patterns for the napoli project.

    Included apps:
    allauth.urls - Handles user authentication (login, signup, etc.).
    admin.site.urls - Django admin panel.
    django_summernote.urls - For Summernote rich text editor.
    booking.urls - Reservation-related views.
    menu.urls - Menu-related views.
    contact.urls - Contact-related views.
    home.urls - Home page views.
"""


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('booking/', include('booking.urls')),
    path('menu/', include('menu.urls')),
    path('contact/', include('contact.urls')),
    path('', include('home.urls')),
]
