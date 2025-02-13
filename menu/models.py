from django.db import models
from cloudinary.models import CloudinaryField

"""
Category model with name and order fields. Categories are ordered by the order field.
"""

class Category(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


"""
Dish model represents a menu item in a restaurant's system.
"""

class Dish(models.Model):

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]

    STATUS = (
        (0, "Draft"),
        (1, "Published")
    )
    
    CURRENCY_CHOICES = [
        ('EUR', '€'),
        ('USD', '$'),
        ('GBP', '£'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EUR')
    category = models.ForeignKey(Category, related_name='menus', on_delete=models.CASCADE)
    image = CloudinaryField(
    "image", 
    blank=True, 
    null=True, 
    help_text="Recommended aspect ratio: 4:3 or 3:2 (e.g., 800×600 px, 1200×900 px, 900×600 px)."
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    publishing_status = models.IntegerField(choices=STATUS, default=1)
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']
    
    def price_with_currency(self):
        return f"{self.get_currency_display()}{self.price}"

    price_with_currency.short_description = 'Price'
    
    def __str__(self):
        return self.name