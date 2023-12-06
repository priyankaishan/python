# myapp_images/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pname', 'price', 'stock', 'image']
