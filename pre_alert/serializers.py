from rest_framework import serializers
from .models import PreAlert

class PreAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAlert
        fields = '__all__'
