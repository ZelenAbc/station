from django import forms
from kiosk.models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = [
            'product',
            'quantity',
        ]
        widgets = {
            'product': forms.HiddenInput(),
            'quantity': forms.HiddenInput(),
        }
