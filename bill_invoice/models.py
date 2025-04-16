from django.db import models

from item.models import Itemstock

class Vendor(models.Model):
          vendor_code = models.CharField(max_length=50, blank=True, null=True)
          vendor_name = models.CharField(unique=True, max_length=250, blank=True, null=True)
          address = models.TextField(blank=True, null=True)
          gst_number = models.CharField(max_length=15, blank=True, null=True)
          pan = models.CharField(max_length=15, blank=True, null=True)
          state = models.CharField(max_length=50, blank=True, null=True)
          state_code = models.CharField(max_length=50, blank=True, null=True)
          phone_number = models.CharField(max_length=10, blank=True, null=True)
          p_no = models.CharField(max_length=50, blank=True, null=True)

          class Meta:
                    db_table = 'vendor'

class Billinvoice(models.Model):
          invoice_number = models.AutoField(primary_key=True)
          vendor_name = models.CharField(max_length=250, blank=True, null=True)
          gst_no = models.CharField(max_length=50, blank=True, null=True)
          consignee_name = models.CharField(max_length=255, blank=True, null=True)
          consignee_state_code = models.CharField(max_length=10, blank=True, null=True)
          consignee_address = models.TextField(blank=True, null=True)
          remarks = models.TextField(blank=True, null=True)
          invoice_date = models.CharField(max_length=50, blank=True, null=True)
          challan_number = models.CharField(max_length=50, blank=True, null=True)
          challan_date = models.CharField(max_length=50, blank=True, null=True)
          order_number = models.CharField(max_length=50, blank=True, null=True)
          order_date = models.CharField(max_length=50, blank=True, null=True)
          veh_no = models.CharField(max_length=50, blank=True, null=True)
          transport_mode = models.CharField(max_length=50, blank=True, null=True)
          due_on = models.CharField(max_length=50, blank=True, null=True)
          time_of_supply = models.CharField(max_length=50, blank=True, null=True)
          payment_terms = models.CharField(max_length=50, blank=True, null=True)
          document = models.CharField(max_length=255, blank=True, null=True)
          delivery_terms = models.CharField(max_length=50, blank=True, null=True)
          transport = models.CharField(max_length=50, blank=True, null=True)
          place_of_supply = models.CharField(max_length=100, blank=True, null=True)
          l_r_number = models.CharField(max_length=50, blank=True, null=True)
          l_r_date = models.CharField(max_length=50, blank=True, null=True)
          ref = models.CharField(max_length=100, blank=True, null=True)
          total_amount = models.FloatField(blank=True, null=True)

          class Meta:
                    db_table = 'billinvoice'
