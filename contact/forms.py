from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """
    A form for creating a single review.
    """
    class Meta:
        model = Review
        fields = ['rating', 'body',]