from django.db import models
from django.contrib.auth.models import User  # type: ignore
from django.core.validators import MaxValueValidator, MinValueValidator

"""
Review model for storing user reviews with rating (1-5),
body, approval status, and timestamps.
"""


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating must be between 1 and 5"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Review by {self.author.username} - {self.rating}⭐"
