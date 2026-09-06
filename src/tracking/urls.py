from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.weight_dashboard, name='weight_dashboard'),
    path('log-weight/', views.log_weight, name='log_weight'),
    path('history/', views.weight_history, name='weight_history'),
]
