from django.db import models
from django.contrib.auth.models import User

class Concert(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    available_tickets = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # NEW SECURE FIELD: Only validates true image files. 
    # 'blank=True, null=True' means existing concerts without posters won't break the database!
    poster = models.ImageField(upload_to='concert_posters/', blank=True, null=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    # This links the booking to a specific User and a specific Concert
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    tickets_booked = models.IntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.concert.title}"
    
class AuditLog(models.Model):
    # We allow 'null=True' because a failed login attempt might be from a user that doesn't exist!
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.action}"

class Profile(models.Model):
    # This links the profile to the user exactly one-to-one
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}'s Profile"