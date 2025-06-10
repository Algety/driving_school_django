from allauth.account.forms import SignupForm
from django import forms
from .models import Student

class CustomSignupForm(SignupForm):
    age = forms.IntegerField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    def save(self, request):
        user = super().save(request)  # Save the default User model
        Student.objects.create(
            user=user,
            age=self.cleaned_data['age'],
            phone_number=self.cleaned_data['phone_number']
        )
        return user