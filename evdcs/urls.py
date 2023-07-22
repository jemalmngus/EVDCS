# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Add other URL patterns for other views if needed
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
