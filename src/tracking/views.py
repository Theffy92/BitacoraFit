from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeightEntry
from .forms import WeightEntryForm

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
        'recent_entries': recent_entries,
        'total_entries': weight_entries.count(),
    })


@login_required
def log_weight(request):
    if request.method == "POST":
        form = WeightEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect("weight_dashboard")
    else:
        form = WeightEntryForm()

    return render(request, "tracking/log_weight.html", {"form": form})

@login_required
def weight_history(request):
    user = request.user
    weight_entries = WeightEntry.objects.filter(user=user)
    return render(request, "tracking/weight_history.html", {
        "weight_entries": weight_entries
    })