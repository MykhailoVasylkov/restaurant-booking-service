from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """
    A form for creating a single review.
    """
    rating = forms.IntegerField(min_value=1, max_value=5, required=True)
    
    class Meta:
        model = Review
        fields = ['author', 'rating', 'body',]
