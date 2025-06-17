from django import forms
from student.models import Profile

# class Registration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

class Registration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','password']
        labels = {'name':'Enter Name','email':'Enter Email','password':'Password'}
        error_messages = {'email':{'required':'Email is required'}}
        widgets = {
            'password': forms.PasswordInput
        }


