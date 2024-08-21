from django import forms

class contactform(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    body = forms.CharField(widget= forms.Textarea)
    