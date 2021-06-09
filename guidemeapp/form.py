from django import forms
from .models import Pesanan
from django.forms import ModelForm

class PesananForm(forms.ModelForm):
    class Meta:
        model = Pesanan
        fields=('pelanggan','tour_guide','lokasi')