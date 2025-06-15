from django.urls import path
from .views import my_booking, booking_new, booking_edit, booking_delete

urlpatterns = [
    path('my_booking/', my_booking, name="my_booking"),
    path('booking_new/', booking_new, name="booking_new"),
    path('booking/edit/<int:pk>/', booking_edit, name='booking_edit'),
    path('booking/delete/<int:pk>/', booking_delete, name='booking_delete'),

]