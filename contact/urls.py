from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_create, name='contact'),
    path('edit/<int:pk>', views.edit_review, name='edit_review'),
]