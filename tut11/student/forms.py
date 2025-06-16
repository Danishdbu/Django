from django import forms


class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        # name_value = self.cleaned_data.get('name')
        name_value = self.cleaned_data['name']
        if len(name_value) < 4:
            raise forms.ValidationError('Enter more than or equal 4 char')
        return name_value


