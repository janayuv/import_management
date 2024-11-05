from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'  # or list the specific fields you want

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")

        # Check for duplicate supplier by name
        if Supplier.objects.filter(name=name).exists():
            raise forms.ValidationError("A supplier with this name already exists.")

        # Check for duplicate email
        if Supplier.objects.filter(email=email).exists():
            raise forms.ValidationError("A supplier with this email already exists.")
        
        return cleaned_data
