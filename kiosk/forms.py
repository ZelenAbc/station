from django import forms
from kiosk.models import Sale


class ProductsListForm(forms.Form):
    products_list = forms.CharField(widget=forms.HiddenInput(), max_length=1024)


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity']
