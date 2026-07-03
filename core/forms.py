from django import forms
from .models import Owner, Cat, Application

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