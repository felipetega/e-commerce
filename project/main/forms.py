from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = Cliente
    fields = "__all__"