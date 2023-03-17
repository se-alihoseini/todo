from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput())
    password = forms.CharField(max_length=40, widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput())
    password = forms.CharField(max_length=40, widget=forms.PasswordInput())
