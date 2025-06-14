from django.db import models
from django.contrib.auth.models import User

class LessonBooking(models.Model):
    LOCATION_CHOICES = [
        ('Cardigan', 'Cardigan'),
        ('Carmarthen', 'Carmarthen'),
        ('Aberystwyth', 'Aberystwyth'),
    ]

    TIME_SLOT_CHOICES = [
        ('08:00-10:00', '08:00 - 10:00'),
        ('10:00-12:00', '10:00 - 12:00'),
        ('12:00-14:00', '12:00 - 14:00'),
        ('14:00-16:00', '14:00 - 16:00'),
        ('16:00-18:00', '16:00 - 18:00'),
        ('18:00-20:00', '18:00 - 20:00'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default="Cardigan")
    date = models.DateField()
    time_slot = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES, default="08:00-10:00")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['location', 'date', 'time_slot'], name='booking_unique')
        ]

    def __str__(self):
        return f"{self.user} - {self.location} on {self.date} at {self.time_slot}"