from django.shortcuts import render
from django.contrib.auth.models import User
from .models import WeightEntry

# Create your views here.
def weight_dashboard(request):
    # For demonstration/development purposes, if no user is authenticated, we use 'testuser'
    user = request.user
    if not user.is_authenticated:
        user = User.objects.get(username='testuser')
        
    # Fetching all weight entries
    weight_entries = WeightEntry.objects.filter(user=user).order_by('-date', "-created_at")
    latest_entry = weight_entries.first()  # Get the most recent entry
    recent_entries = weight_entries[1:7]  # Get the next few recent entries
    return render(request, 'tracking/weight_dashboard.html', {
        'latest_entry': latest_entry, 
        'recent_entries': recent_entries
    })
