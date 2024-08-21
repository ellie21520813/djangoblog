from django import forms

class Registerform(forms.Form):
    username= forms.CharField(max_length=25)
    email = forms.EmailField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
class loginform(forms.Form):
    username= forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
