from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['location', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }