from rest_framework import serializers
from bill_invoice.models import Invoice

from rest_framework import serializers
from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_date = serializers.DateField(
        required=False, help_text="Invoice date")
    name = serializers.CharField(
        required=False, min_length=1, max_length=255, help_text="Name")
    gst_no = serializers.CharField(
        required=False, min_length=1, max_length=50, help_text="Gst no")
    consignee_name = serializers.CharField(
        required=False, min_length=1, max_length=255, help_text="Consignee name")
    quantity = serializers.IntegerField(
        required=False, default=0, help_text="Quantity")

    class Meta:
        model = Invoice
        fields = "__all__"

        
from rest_framework import serializers

from .models import Vendor



class VendorSerializer(serializers.ModelSerializer):
    
     pan= serializers.CharField(max_length=15,required=False, help_text="PAN")
     p_no=serializers.CharField( max_length=50,required=False, help_text="P_NO")
     
     class Meta:
        model =Vendor
        fields = "__all__"
