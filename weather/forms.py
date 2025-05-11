from django import forms
from .models import City  # Ensure you have imported your City model

class CityForm(forms.ModelForm):
    class Meta:
        model = City  # Link the form to the City model
        fields = ['name']  # Specify the fields to be included in the form
