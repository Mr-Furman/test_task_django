from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import AppUser
class RegisterForm(UserCreationForm):
   
    class Meta:
        model = AppUser
        fields = ["username", "email"]

class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = ("username", "email",)

class CollectForm(forms.Form):
    csv_file = forms.FileField(required=True)
    xml_file = forms.FileField(required=True)