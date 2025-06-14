from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from .models import LessonBooking
from .forms import BookingForm

@login_required
def my_booking(request):
    bookings = LessonBooking.objects.filter(user=request.user)
    return render(request, 'booking/my_booking.html', {'bookings': bookings})

@login_required
def booking_new(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            # try:
            booking.save()
            messages.success(request, "Booking created successfully!")
            return redirect('my_booking')
            # except Exception as e:
            #     form.add_error(None, "This slot is already booked.")
    else:
        form = BookingForm()
    return render(request, 'booking/booking_new.html', {'form': form})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(LessonBooking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted.")
        return redirect('my_booking')
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})