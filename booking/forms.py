from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['client', 'phone_number', 'date', 'time', 'people_count', 'table_count','comment']
    # Table_count field validation method. I did with chat-gpt 
    def clean_table_count(self):
        people_count = self.cleaned_data.get('people_count')
        if people_count:
            table_count = (people_count + 3) // 4
            return table_count