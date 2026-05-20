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
    # Find the specific concert
    concert = get_object_or_404(Concert, id=concert_id)
    
    if request.method == 'POST':
        # 1. Grab the exact number the user typed into the form
        # Use 'tickets_booked' because that is the name="" attribute in the HTML form
        # Use default to 1 just in case, and wrap it in int() to ensure it's a number
        tickets_requested = int(request.POST.get('tickets_booked', 1))
        
        # 2. Security Check: Make sure user aren't trying to book more than available tikkets.
        if tickets_requested > 0 and tickets_requested <= concert.available_tickets:
            
            # 3. Subtract the exact requested amount
            concert.available_tickets -= tickets_requested
            concert.save()
            
            # 4. Save the booking record with the correct ticket amount
            Booking.objects.create(
                user=request.user,
                concert=concert,
                tickets_booked=tickets_requested
            )
            
            # Send them to their dashboard to see the new tickets
            return redirect('profile')
            
        else:
            # If they try to hack the form to buy 5000 tickets, it just reloads the page safely
            return render(request, 'booking/book_ticket.html', {
                'concert': concert,
                'error': 'Not enough tickets available.' 
            })

    # If it's a GET request (just viewing the page), show the form
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