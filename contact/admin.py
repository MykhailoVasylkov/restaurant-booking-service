from django.contrib import admin
from .models import Review

"""
Register Review model in admin panel.
Add how reviews are displaying.
Add search functionality.
Add filter functionality.
"""


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('author', 'rating', 'created_on', 'approved',)
    search_fields = ['author', 'body', ]
    list_filter = ('rating', 'approved',)
