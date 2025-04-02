from rest_framework import serializers
from .models import Supplier  # Ensure the correct model import

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
