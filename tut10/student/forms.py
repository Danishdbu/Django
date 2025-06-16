from django import forms
from django.forms import DateTimeInput
from django.core.validators import MinLengthValidator,RegexValidator

class DemoForm(forms.Form):
    # Basic Field
    name = forms.CharField()
    email = forms.EmailField()
    pin_code = forms.IntegerField()

    # Additional Field Types
    age = forms.FloatField()
    date_of_birth = forms.TimeField()
    appointment_datetime = forms.DateTimeField(
    widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
)

    is_subscribed = forms.BooleanField()
    agree_terms = forms.NullBooleanField()

    # Choice Field
    gender = forms.ChoiceField(choices=[('M','Male'),('F', 'Female'),('O','other')])
    interests = forms.MultipleChoiceField(choices=[('tech','Technology'),('art','Art'),('sports','Sports')])

    # File and URL Fields

    profile_image = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()

    # Other Specialized Fields

    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    password = forms.CharField(widget=forms.PasswordInput())
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField()
    rating = forms.DecimalField()

