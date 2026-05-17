from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm
from django.contrib.auth import login
from .models import Concert
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Concert, Booking

def concert_list(request):
    concerts = Concert.objects.all()
    return render(request, 'booking/concert_list.html', {'concerts': concerts})

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST) # <-- UPDATED
        if form.is_valid():
            user = form.save()  
            login(request, user)
            return redirect('welcome')
    else:
        form = CustomRegistrationForm() # <-- UPDATED
        
    return render(request, 'booking/register.html', {'form': form})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after they register
            login(request, user)
            return redirect('concert_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'booking/register.html', {'form': form})

# This security decorator ensures ONLY logged-in users can trigger this function
@login_required
def book_ticket(request, concert_id):
    # Securely fetch the exact concert, or show a safe 404 error if it doesn't exist
    concert = get_object_or_404(Concert, id=concert_id)
    
    if request.method == 'POST':
        # Create a new booking linking the logged-in user to this concert
        Booking.objects.create(
            user=request.user,
            concert=concert,
            tickets_booked=1
        )
        # Deduct the ticket from the available inventory
        concert.available_tickets -= 1
        concert.save()
        
        # Send them back to the homepage for now
        return redirect('concert_list')
        
    return render(request, 'booking/book_ticket.html', {'concert': concert})
@login_required
def profile(request):
    # Securely fetch ONLY the bookings associated with the currently logged-in user
    user_bookings = Booking.objects.filter(user=request.user)
    
    return render(request, 'booking/profile.html', {'bookings': user_bookings})

from django.contrib.auth.decorators import login_required

# Requires the user to be logged in to see the welcome page
@login_required
def welcome_page(request):
    return render(request, 'booking/welcome.html')