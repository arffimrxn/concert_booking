from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomRegistrationForm(UserCreationForm):
    # Add our extra fields to the form
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True, min_value=13, help_text="You must be at least 13 to register.")
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        # Tell Django to include the email field on the base User model
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        # 1. Save the base User (username, password, email)
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # 2. Create the linked Profile with the remaining data
            Profile.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                phone_number=self.cleaned_data['phone_number']
            )
        return user