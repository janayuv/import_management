from django.contrib import admin
from .models import ItemMaster

@admin.register(ItemMaster)
class ItemMasterAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'part_number', 'part_description', 'unit', 'price', 'cth', 'bcd', 'sws', 'igst')
    search_fields = ('part_number', 'part_description')
    list_filter = ('supplier',)
