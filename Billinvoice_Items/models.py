from django.db import models
from bill_invoice.models import Billinvoice

# Create your models here.
class Billinvoiceitems(models.Model):
          item_id = models.AutoField(primary_key=True)
          description = models.CharField(max_length=200, blank=True, null=True)
          hsn_code = models.CharField(max_length=30, blank=True, null=True)
          quantity = models.IntegerField(blank=True, null=True)
          unit_rate = models.FloatField(blank=True, null=True)
          discount_percentage = models.FloatField(blank=True, null=True)
          gst_rate = models.FloatField(blank=True, null=True)
          cgst = models.FloatField(blank=True, null=True)
          sgst = models.FloatField(blank=True, null=True)
          igst = models.FloatField(blank=True, null=True)
          total_value = models.FloatField(blank=True, null=True)
          discount_amount = models.FloatField(blank=True, null=True)
          grand_total = models.FloatField(blank=True, null=True)
          invoice_number = models.ForeignKey(Billinvoice, models.DO_NOTHING, db_column='invoice_number',
                                             related_name='items')

          class Meta:
                    db_table = 'billinvoiceitems'
