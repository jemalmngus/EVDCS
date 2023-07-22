# authentication/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Add other URL patterns for authentication views as needed
]
