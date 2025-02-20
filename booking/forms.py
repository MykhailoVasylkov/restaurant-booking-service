import re
from django.core.exceptions import ValidationError
from django import forms
from .models import Reservation

def validate_phone_number(value):
    """Validate phone number format."""
    if not re.match(r'^\+?\d{1,15}$', value):
        raise ValidationError("Invalid phone number format")

class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['client', 'phone_number', 'date', 'time', 'people_count', 'table_count', 'comment']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        validate_phone_number(phone_number)  # Apply custom validation
        return phone_number
