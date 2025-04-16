from rest_framework import serializers

from .models import Billinvoice, Vendor
from Billinvoice_Items.serializers import BillItemSerializer

class BillInvoiceSerializer(serializers.ModelSerializer):
          items = BillItemSerializer(many=True, read_only=True)

          class Meta:
                    model = Billinvoice
                    fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
          pan = serializers.CharField(max_length=15, required=False, help_text="PAN")
          p_no = serializers.CharField(max_length=50, required=False, help_text="P_NO")

          class Meta:
                    model = Vendor
                    fields = "__all__"
