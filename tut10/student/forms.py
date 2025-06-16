from django import forms  
from django.forms import DateTimeInput, DateInput  
from django.core.validators import MinLengthValidator, RegexValidator  

# class DemoForm(forms.Form):
#     # Basic Field
#     name = forms.CharField()
#     email = forms.EmailField()
#     pin_code = forms.IntegerField()

#     # Additional Field Types
#     age = forms.FloatField()
#     date_of_birth = forms.TimeField()
#     appointment_datetime = forms.DateTimeField(
#     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
# )

#     is_subscribed = forms.BooleanField()
#     agree_terms = forms.NullBooleanField()

#     # Choice Field
#     gender = forms.ChoiceField(choices=[('M','Male'),('F', 'Female'),('O','other')])
#     interests = forms.MultipleChoiceField(choices=[('tech','Technology'),('art','Art'),('sports','Sports')])

#     # File and URL Fields

#     profile_image = forms.ImageField()
#     resume = forms.FileField()
#     website = forms.URLField()

#     # Other Specialized Fields

#     phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
#     password = forms.CharField(widget=forms.PasswordInput())
#     slug = forms.SlugField()
#     ip_address = forms.GenericIPAddressField()
#     rating = forms.DecimalField()



# Define a form class that inherits from forms.Form
class DemoForm(forms.Form):

    # Text input with max length and min length validation
    name = forms.CharField(
        max_length=100,  # Maximum allowed characters
        validators=[MinLengthValidator(3)],  # Minimum 3 characters required
        label="Full Name",  # Label shown on the form
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Styled as Bootstrap input
    )

    # Email input field with email validation
    email = forms.EmailField(
        label="Email",  # Label for email field
        widget=forms.EmailInput(attrs={'class': 'form-control'})  # Email widget with styling
    )

    # Integer input for postal code with min and max value limits
    pin_code = forms.IntegerField(
        min_value=1000,  # Minimum value allowed
        max_value=999999,  # Maximum value allowed
        label="Postal Code"  # Label shown on the form
    )

    # Integer input for age with value constraints
    age = forms.IntegerField(
        min_value=0,  # Minimum age allowed
        max_value=100,  # Maximum age allowed
        label="Age"  # Label shown on the form
    )

    # Date input using a date picker
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})  # HTML5 date input
    )

    # Date and time input using a datetime-local picker
    appointment_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})  # DateTime picker
    )

    # Boolean checkbox input (optional)
    is_subscribed = forms.BooleanField(
        required=False,  # Optional field
        label="Subscribe to Newsletter"  # Label shown on the form
    )

    # Dropdown select for three states: Yes, No, Unknown (NullBooleanField)
    agree_terms = forms.NullBooleanField(
        widget=forms.Select(attrs={'class': 'form-select'})  # Dropdown styling with Bootstrap
    )

    # Radio button selection for gender
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],  # Dropdown or radio choices
        widget=forms.RadioSelect  # Displayed as radio buttons
    )

    # Multiple checkboxes for interest selection
    interests = forms.MultipleChoiceField(
        choices=[('tech', 'Technology'), ('art', 'Art'), ('sports', 'Sports')],  # Multiple choices
        widget=forms.CheckboxSelectMultiple  # Displayed as checkboxes
    )

    # File upload input for image (optional)
    profile_image = forms.ImageField(
        required=False,  # Optional image field
        widget=forms.FileInput(attrs={'accept': 'image/*'})  # Accept only image file types
    )

    # File upload input for resume documents (optional)
    resume = forms.FileField(
        required=False,  # Optional file field
        widget=forms.FileInput(attrs={'accept': '.pdf,.doc,.docx'})  # Accept only specific file types
    )

    # Optional URL field with validation
    website = forms.URLField(
        required=False,  # Optional field
        label="Website"  # Label shown on the form
    )

    # Regex validated phone number field with placeholder
    phone_number = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',  # Regex for validating international phone number format
        label="Phone Number",  # Label shown on the form
        error_messages={'invalid': 'Invalid phone number'},  # Custom error message
        widget=forms.TextInput(attrs={'placeholder': '+123456789'})  # Placeholder example
    )

    # Password field with minimum length and hidden input
    password = forms.CharField(
        min_length=8,  # Minimum password length
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  # Password input with hidden characters
    )

    # Slug input for URLs
    slug = forms.SlugField(
        max_length=50,  # Max length of slug
        label="URL Slug"  # Label shown on the form
    )

    # IP address input, restricted to IPv4
    ip_address = forms.GenericIPAddressField(
        protocol='IPv4',  # Restrict to IPv4 addresses
        label="IPv4 Address"  # Label shown on the form
    )

    # Decimal input for rating with value and format constraints
    rating = forms.DecimalField(
        max_digits=4,  # Max total digits
        decimal_places=2,  # Digits after decimal point
        min_value=0,  # Minimum value
        max_value=10.0,  # Maximum value
        label="Rating"  # Label shown on the form
    )
