from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_text',)

class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())