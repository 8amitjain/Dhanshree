from django import forms

from .models import ProductContact


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductContact
        fields = ['name', 'email', 'mobile']


