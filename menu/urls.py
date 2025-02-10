from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_by_category, name='menu'),
]