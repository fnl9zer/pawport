from django import forms
from django.contrib.auth.models import User
from .models import Owner, Cat, Application

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        username = cleaned_data.get("username")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match!")
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken, please choose another!")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken, please choose another!")
        email = cleaned_data.get('email')
        if email and Owner.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered, please login instead!")
        return cleaned_data

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'email', 'phone']

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'breed', 'age', 'is_neutered', 'vaccination_record', 'landlord_reference', 'photo']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cat', 'message']