from django import forms
from .models import VendorAdd

class VendorAddForm(forms.ModelForm):
    class Meta:
        model = VendorAdd
        fields = '__all__'
        