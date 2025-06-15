from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import LessonBooking
from .forms import BookingForm
from datetime import date

@login_required
def my_booking(request):
    today = date.today()
    bookings = LessonBooking.objects.filter(user=request.user, date__gte=today).order_by('location','date','time_slot')
    return render(request, 'booking/my_booking.html', {'bookings': bookings})

@login_required
def booking_new(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            location = form.cleaned_data['location']
            time_slot = form.cleaned_data['time_slot']

            if LessonBooking.objects.filter(date=date, location=location, time_slot=time_slot).exists():
                messages.error(request, "This time slot is not available.")
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.success(request, "Booking created successfully!")
                return redirect('my_booking')
        else:
            messages.error(request, "Please check the form and try again.")
    else:
        form = BookingForm()
    return render(request, 'booking/booking_new.html', {'form': form})

@login_required
def booking_edit(request, pk):
    """
    view to edit booking
    """
    booking = get_object_or_404(LessonBooking, pk=pk, user=request.user)
    booking_form = BookingForm(request.POST, instance=booking)
    
    if request.method == "POST":  
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)

            if LessonBooking.objects.filter(date=booking.date, location=booking.location, time_slot=booking.time_slot).exclude(pk=pk).exists():
                messages.error(request, "This time slot is not available.")
            else:
                booking.save()
                messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
                return redirect('my_booking')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    else:
        booking_form = BookingForm(instance=booking)
    # return HttpResponseRedirect(reverse('my_booking'))
    return render(request, 'booking/booking_edit.html', {'form': booking_form})


@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(LessonBooking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted.")
    return redirect('my_booking')
   