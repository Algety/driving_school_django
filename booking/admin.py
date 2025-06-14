from django.contrib import admin
from .models import LessonBooking
from students.models import Student


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'get_first_name',
        'get_last_name',
        'get_phone_number',
        'location',
        'date',
        'time_slot',
    )
    list_filter = ('location', 'date', 'time_slot')
    list_editable = (
        'location',
        'date',
        'time_slot',
    )
    search_fields = (
            'user__username',
            'user__student__last_name',
            'location',
            'date'
    )

    def get_first_name(self, obj):
        try:
            return obj.user.student.first_name
        except Student.DoesNotExist:
            return ''
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        try:
            return obj.user.student.last_name
        except Student.DoesNotExist:
            return ''
    get_last_name.short_description = 'Last Name'

    def get_phone_number(self, obj):
        try:
            return obj.user.student.phone_number
        except Student.DoesNotExist:
            return ''
    get_phone_number.short_description = 'Phone Number'

admin.site.register(LessonBooking, BookingAdmin)