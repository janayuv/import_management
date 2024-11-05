from django import forms
from .models import ItemMaster
from django import forms

class ItemMasterForm(forms.ModelForm):
    class Meta:
        model = ItemMaster
        fields = ['supplier', 'part_number', 'part_description', 'unit', 'price', 'bcd', 'sws', 'igst', 'cth']

class ExcelUploadForm(forms.Form):
    file = forms.FileField()