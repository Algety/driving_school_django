from django.urls import path
from .views import booking_list, booking_create

urlpatterns = [
    path('my_booking/', booking_list, name="my_booking"),
    path('booking_new/', booking_create, name="booking_new"),
]