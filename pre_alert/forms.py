from django import forms
from .models import PreAlert

class PreAlertForm(forms.ModelForm):
    class Meta:
        model = PreAlert
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'bl_awb_date': forms.DateInput(attrs={'type': 'date'}),
            'etd': forms.DateInput(attrs={'type': 'date'}),
            'eta': forms.DateInput(attrs={'type': 'date'}),
            'boe_date': forms.DateInput(attrs={'type': 'date'}),
        }
