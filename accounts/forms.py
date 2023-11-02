from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class UserAdminCreationForm(UserCreationForm):
    """A custom form for creation new users."""

    required_css_class = ...
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']