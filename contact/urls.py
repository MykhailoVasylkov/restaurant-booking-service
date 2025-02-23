from django.urls import path
from . import views

"""
URL patterns for review management: 
1. Create review (contact page), 2. Edit review, 3. Delete review.
"""


urlpatterns = [
    path('', views.review_create, name='contact'),
    path('edit/<int:pk>', views.edit_review, name='edit_review'),
    path('delete/<int:pk>', views.delete_review, name='delete_review'),
]
