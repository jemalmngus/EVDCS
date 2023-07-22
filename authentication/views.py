from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import RegistrationForm
class RegistrationView(TemplateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class LoginCustomView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('dashboard')
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # User is already authenticated, redirect to the dashboard
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)
