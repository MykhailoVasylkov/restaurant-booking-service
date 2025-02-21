from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class Reservation(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Confirmed'),
        (2, 'Cancelled'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    phone_number = models.CharField(
        max_length=15,
        validators=[MaxLengthValidator(15)]
    )
    date = models.DateField()
    time = models.TimeField()
    people_count = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    table_count = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    
    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f'Reservation by {self.client.username} on {self.date} at {self.time}'