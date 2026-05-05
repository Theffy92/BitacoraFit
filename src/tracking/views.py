from django.shortcuts import render
from .models import WeightEntry
# Create your views here.
def weight_dashboard(request):
    # Fetching all weight entries
    weight_entries = WeightEntry.objects.filter(user=request.user).order_by('-date', "created_at")
    latest_entry = weight_entries.first()  # Get the most recent entry
    recent_entries = weight_entries[1:6]  # Get the next 5 recent entries after the latest one
    return render(request, 'tracking/weight_dashboard.html', {'latest_entry': latest_entry, 'recent_entries': recent_entries})
