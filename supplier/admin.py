# supplier/admin.py

from django.contrib import admin
from .models import Supplier
from .admin_forms import SupplierAdminForm

class SupplierAdmin(admin.ModelAdmin):
    form = SupplierAdminForm
    list_display = [
        'name', 'contact_person', 'email', 'phone', 'country'
    ]
    search_fields = [
        'name', 'contact_person', 'email', 'phone', 'country'
    ]
    ordering = ['name']
    list_filter = ['country']

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Supplier Details', {
            'fields': (
                'address1', 'address2', 'address3',
                'country', 'zipcode'
            )
        }),
        ('Contact Details', {
            'fields': (
                'contact_person', 'email', 'phone', 'tax_id'
            )
        }),
        ('Remittance Details', {
            'fields': (
                'bank', 'bank_address', 'branch',
                'account_number', 'swift_code'
            )
        }),
    )

admin.site.register(Supplier, SupplierAdmin)
