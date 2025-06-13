from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, default=None, null=True, blank=True)
    last_name = models.CharField(max_length=150, default=None, null=True, blank=True)
    phone_number = models.CharField(max_length=15, default=None, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    booked_test_day = models.DateField(default=None, null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} (Student)"



