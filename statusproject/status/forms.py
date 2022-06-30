from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Location
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

# Form to build a WorkRequest.


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('location', 'message',)

        def form_valid(self, form_class):
            form_class.instance.user = self.request.user
            return super().form_valid(form)
