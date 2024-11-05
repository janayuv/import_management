from rest_framework import serializers
from .models import ItemMaster

class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = ['id', 'supplier', 'part_number', 'part_description', 'unit', 'price', 'bcd', 'sws', 'igst', 'cth']
