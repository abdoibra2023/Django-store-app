from django import forms
from .models import VendorAdd

class VendorAddForm(forms.ModelForm):
    class Meta:
        model = VendorAdd
        fields = [  
            "add_prod_name", 
            "company_name", 
            "vendor_email", 
            "product_images", 
            "product_description", 
            "product_price", 
            "product_categ"
        ]

