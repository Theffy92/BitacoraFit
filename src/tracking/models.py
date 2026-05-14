from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WeightEntry(models.Model):
    #defining the fields for the weight entry model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    #Storing weight in pounds with up to 2 decimal places
    #idea: Convert it to kilograms in the view (UI) if needed, but store it in pounds for consistency
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}: {self.weight} lbs"
    
    class Meta:
        ordering = ['-date', '-created_at']  # Default ordering by date and creation time, newest first
