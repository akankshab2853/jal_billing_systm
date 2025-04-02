from django.db import models

# Create your models here.
class Supplier(models.Model):
   
    supplier_code= models.CharField(max_length=50, blank=True, null=True)
    supplier_name = models.CharField(max_length=250, blank=True, null=True)
    pan=models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    p_no=models.CharField( max_length=50)

    def __str__(self):
        return self.vendor_name