# supplier/admin_forms.py

from django import forms
from .models import Supplier

class SupplierAdminForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'name', 'address1', 'address2', 'address3',
            'country', 'zipcode',
            'contact_person', 'email', 'phone', 'tax_id',
            'bank', 'bank_address', 'branch', 'account_number', 'swift_code'
        ]
