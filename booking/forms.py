from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    # NEW: Date of Birth field with the calendar widget!
    date_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}), # This triggers the HTML5 calendar
        help_text="You must be at least 13 years old to register."
    )
    
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                # NEW: Save the date of birth instead of age
                date_of_birth=self.cleaned_data['date_of_birth'], 
                phone_number=self.cleaned_data['phone_number']
            )
        return user