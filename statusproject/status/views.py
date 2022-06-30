from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Location
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['location', 'message']
    template_name = 'status/location_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Home(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'login'
    model = Location
    template_name = 'status/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_employee_location'] = Location.objects.filter(
            user=self.request.user)
        context['all_stats'] = Location.objects.all()
        context['only_user'] = Location.objects.filter(
            user=self.request.user).count()
        context['empty_message'] = Location.objects.filter(
            message__isnull=True)
        context['has_message'] = Location.objects.exclude(message__isnull=True)
        context[last_seen] = Location.objects.filter(timestamp)
        return context


class LocationDetailView(DetailView):
    model = Location
    template_name = 'status/location_detail.html'


class LocationUpdateView(UpdateView):
    model = Location
    fields = ['location', 'message']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')
