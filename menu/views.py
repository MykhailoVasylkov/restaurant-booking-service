from django.shortcuts import render
from .models import Dish, Category

"""
I used Chat-GPT
"""


def menu_by_category(request):
    """
    Display all dishes with the 'available' status grouped by category.

    **Context**

    ``menu_categories``
    A list of dictionaries with categories and their corresponding dishes.

    **Template:**

    :template:`menu/menu_page.html`
    """
    # Get all dishes with the 'available' status
    queryset = Dish.objects.filter(publishing_status=1)

    # Fetch all categories from the database
    categories = Category.objects.all().order_by('order')

    # Prepare a list of categories with their corresponding dishes
    menu_categories = []
    for category in categories:
        # Fetch dishes belonging to this category and marked as 'available'
        dishes = queryset.filter(category=category).order_by('order')
        menu_categories.append({
            'category': category,   # Category instance
            'dishes': dishes,       # QuerySet of dishes in this category
        })

    # Pass the gathered data to the template
    return render(
        request, 'menu/menu_page.html', {'menu_categories': menu_categories}
    )
