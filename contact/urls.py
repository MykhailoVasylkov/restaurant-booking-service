from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_create, name='contact_us'),
]