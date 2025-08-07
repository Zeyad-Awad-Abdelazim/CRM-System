from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import UserRecord

# Registration Form Class
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login Form Class
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)

# Record Form
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ['f_name', 'l_name', 'phone', 'category', 'tall', 'width', 'addres']


# Update record form
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ['f_name', 'l_name', 'phone', 'category', 'tall', 'width', 'addres']
