from django import forms
from django.contrib.auth.models import User

from .models import  Products


class ProductForm(forms.ModelForm):

    class Meta:
       model = Products
       fields = ['product_name', 'price','category','subcategory']

