from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import WeightEntry

# Create your views here.
@login_required
def weight_dashboard(request):
    # For demonstration/development purposes, if no user is authenticated, we use 'testuser'
    user = request.user

    # Fetching all weight entries
    # Since I added ordering in the model's Meta class, the entries will be ordered by date and creation time, newest first
    weight_entries = WeightEntry.objects.filter(user=user)
    latest_entry = weight_entries.first()  # Get the most recent entry
    recent_entries = weight_entries[1:7]  # Get the next few recent entries
    return render(request, 'tracking/weight_dashboard.html', {
        'latest_entry': latest_entry,
        'recent_entries': recent_entries
    })
