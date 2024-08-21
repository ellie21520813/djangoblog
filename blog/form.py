from django import forms

class imageblogform(forms.Form):
    blog_title = forms.CharField(max_length=255)
    blog_image = forms.FileField()
    blog_body = forms.CharField(widget=forms.Textarea)