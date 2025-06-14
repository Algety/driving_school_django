from django.urls import path
from .views import my_booking, booking_new

urlpatterns = [
    path('my_booking/', my_booking, name="my_booking"),
    path('booking_new/', booking_new, name="booking_new"),
]