from django import forms
from .models import User, Blog

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["userName", "password"]

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["userId", "title", "description", "visibility", "image"]