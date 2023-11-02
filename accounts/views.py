from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

from django.views.generic import CreateView

from .models import CustomUser
from .forms import UserAdminCreationForm

User = get_user_model()


class UserCreateView(CreateView):
    """
    View for creating a new object, with a response render by a template.
    """
    
    model = CustomUser
    template_name = 'register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')
    permission_required = None
