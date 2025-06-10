from django.contrib.auth.models import User
from django.db import models
import datetime


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    booked_test_day = models.DateField(default=None, null=True, blank=True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Student)"



