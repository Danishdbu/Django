from django import forms
from account.models import User
class RegistrationForm(forms.ModelForm):
    password = forms.CharField (widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ["email", "name", "password", "confirm_password"]