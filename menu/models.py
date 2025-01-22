from django.db import models
from cloudinary.models import CloudinaryField

class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('Pizza', 'Pizza'),
        ('Pasta', 'Pasta'),
        ('Lasagna', 'Lasagna'),
        ('Starters', 'Starters'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
        ('Other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    
    STATUS = (
        (0, "Draft"),
        (1, "Published")
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = CloudinaryField('image', default='placeholder')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    publishing_status = models.IntegerField(choices=STATUS, default=1)
    
    def price_with_currency(self):
        return f"€{self.price}"

    price_with_currency.short_description = 'Price'

    def __str__(self):
        return self.name