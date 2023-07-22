# authentication/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginCustomView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
