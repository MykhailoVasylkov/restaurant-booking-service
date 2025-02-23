from django.urls import path
from . import views

"""
    URL pattern for the menu by category.

    **View:**
    ``menu_by_category`` - Displays the menu filtered by category.

    **Template:**
    :template:`menu/menu_by_category.html`
"""


urlpatterns = [
    path('', views.menu_by_category, name='menu'),
]
