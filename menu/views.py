from django.shortcuts import render
from .models import Menu


def menu_by_category(request):
    """
    Display all dishes with the 'available' status.

    **Context**

    ``menu_categories``
    A list :model:`menu.Menu` instances filtered by category.

    **Template:**
    
    :template:`menu/menu_page.html`
    """
    # Get all dishes with the 'available' status
    queryset = Menu.objects.filter(publishing_status=1)

    # Prepare a list of categories with their corresponding dishes
    menu_categories = []
    for category_code, category_display in Menu.CATEGORY_CHOICES:
        # Fetch dishes belonging to this category and marked as 'available'
        dishes = queryset.filter(category=category_code)
        menu_categories.append({
            'code': category_code,         # Category code (e.g., 'Pizza')
            'display': category_display,   # Display name of the category (e.g., 'Pizza')
            'dishes': dishes,              # QuerySet of dishes in this category
        })

    # Pass the gathered data to the template
    return render(request, 'menu/menu_page.html', {'menu_categories': menu_categories})
