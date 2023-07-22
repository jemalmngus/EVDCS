# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            roll = form.cleaned_data.get('roll')
            # Add logic to handle registration based on the selected roll
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your homepage
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
