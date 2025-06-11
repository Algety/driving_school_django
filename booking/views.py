from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from datetime import datetime, timedelta

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.date >= datetime.today().date() + timedelta(days=1):
                booking.save()
                return redirect('booking_success')
            else:
                form.add_error('date', 'Booking date must be at least tomorrow.')
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})