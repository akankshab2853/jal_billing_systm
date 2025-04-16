from rest_framework import serializers
from Billinvoice_Items.models import Billinvoiceitems

class BillItemSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Billinvoiceitems
                    fields = '__all__'

          def to_representation(self, instance):
                    representation = super().to_representation(instance)
                    # Remove 'invoice_number' from the representation
                    representation.pop('invoice_number', None)
                    return representation
