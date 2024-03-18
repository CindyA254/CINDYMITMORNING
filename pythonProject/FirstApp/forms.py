from django import forms
from .models import Register
class FirstAppForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Enter your Name")
    age = forms.IntegerField(min_value=18, label="Enter your age")
    check = forms.BooleanField(required=False, label="Do you wnt to join us")
    check = forms.ChoiceField(choices=[('student', 'student'), ('teacher', 'teacher'), ('Administrator', 'Administrator')])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
class RegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=100, required=True, label="Enter your first Name")
    lastname = forms.CharField(max_length=100, required=True, label="Enter your last name")
    age = forms.IntegerField(min_value=18, label="Enter your age")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ['firstname', 'lastname', 'email', 'password']
