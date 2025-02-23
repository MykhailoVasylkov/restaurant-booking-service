from django.urls import path
from . import views

"""
    URL pattern for the home page.

    **View:**
    ``home_page`` - Renders the home page.

    **Template:**
    :template:`home/home.html`
"""


urlpatterns = [
    path('', views.home_page, name='home'),
]
