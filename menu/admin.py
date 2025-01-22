from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Menu

"""
Register Menu model in admin panel.
Add how menu items is displaying.
Add search functionality.
Add filter functionality.
Add summernote functionality to content field.
"""
@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('name', 'category', 'price', 'currency', 'status', 'publishing_status')
    search_fields = ['name', 'description']
    list_filter = ('category', 'status', 'publishing_status', 'price')
    summernote_fields = ('description',)

