from django import forms
from .models import LessonBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = LessonBooking
        fields = ['location', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date(self):
        booking_date = self.cleaned_data['date']
        tomorrow = date.today() + timedelta(days=1)

        if booking_date < tomorrow:
            raise forms.ValidationError("You can only book lessons starting from tomorrow.")

        return booking_date
