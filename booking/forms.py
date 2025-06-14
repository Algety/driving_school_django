from django import forms
from .models import LessonBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = LessonBooking
        fields = ['location', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }