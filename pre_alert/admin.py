from django.contrib import admin
from .models import PreAlert

class PreAlertAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Invoice Details', {
            'fields': ('supplier', 'invoice_no', 'date', 'goods', 'currency', 'inv_value')
        }),
        ('BL/AWB Information', {
            'fields': ('bl_awb_no', 'bl_awb_date', 'weight', 'etd', 'eta', 'forwarder', 'incoterm', 'mode', 'kind_of', 'container_no', 'vsl')
        }),
        ('BOE Details', {
            'fields': ('boe_no', 'boe_date', 'ex_rate', 'dutypaid', 'boe_frt', 'boe_exw')
        }),
    )

    list_display = (
        'invoice_no', 'supplier', 'date', 'goods', 'inv_value',
        'bl_awb_no', 'weight', 'etd', 'eta', 'kind_of', 'container_no', 'vsl',
        'boe_no', 'boe_date', 'ex_rate', 'dutypaid', 'boe_frt', 'boe_exw'
    )

    list_filter = ('supplier', 'mode', 'incoterm', 'forwarder', 'kind_of')
    search_fields = ('invoice_no', 'supplier__name', 'bl_awb_no')
    ordering = ('-date',)

    class Media:
        css = {
            'all': ('pre_alert/static/css/custom_admin.css',)
        }

admin.site.register(PreAlert, PreAlertAdmin)

