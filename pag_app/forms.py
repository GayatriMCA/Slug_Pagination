from django import forms
from pag_app.models import Blog_Website

class Blog_WebsiteForm(forms.ModelForm):
    class Meta:
        model = Blog_Website
        fields = ('Author', 'Title', 'Description', )