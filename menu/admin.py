from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import Dish, Category

"""
Register Dish model in admin panel.
Add how menu items is displaying.
Add search functionality.
Add filter functionality.
Add summernote functionality to content field.
Add SortableAdminMixin functionality to order positions inside categories
"""
@admin.register(Dish)
class DishAdmin(SortableAdminMixin, SummernoteModelAdmin, admin.ModelAdmin):

    list_display = ('name', 'category', 'price', 'currency', 'status', 'publishing_status', 'order')
    ordering = ['order']
    search_fields = ['name', 'description']
    list_filter = ('category', 'status', 'publishing_status', 'price')
    summernote_fields = ('description',)

"""
Register Categoryh model in admin panel.
Add how category items is displaying.
Add SortableAdminMixin functionality to order positions inside categories
"""

@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ['order']