from django import forms

class imageblogform(forms.Form):
    title_blog = forms.CharField(max_length=255)
    blog_image = forms.FileField()
    content_blog = forms.CharField(widget=forms.Textarea)
    author_blog = forms.CharField(max_length=255)
class commentform(forms.Form):
    body = forms.CharField(widget=forms.Textarea)