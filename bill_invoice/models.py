from django.db import models

from django.db import models

# Create your models here.

class Vendor(models.Model):
   
    vendor_code= models.CharField(max_length=50, blank=True, null=True,default="000000")
    vendor_name = models.CharField(max_length=250, blank=True, null=True, default="Unknown Vendor")
    address = models.TextField(blank=True, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    pan=models.CharField(max_length=15)
    state = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    p_no=models.CharField( max_length=50)

    class Meta:
        managed = False
        db_table = 'bill_invoice_vendor'

    def __str__(self):
        return self.vendor_name


class Invoice(models.Model):
    TRANSPORT_MODES = [
        ("road", "Road"),
        ("rail", "Rail"),
        ("air", "Air"),
        ("ship", "Ship"),
        ("other", "Other"),
    ]

    invoice_number = models.CharField(max_length=50, unique=True, editable=False)
    invoice_date = models.DateField()
    name = models.CharField(max_length=255, unique=True,blank=True, null=True)
    gst_no = models.CharField(max_length=50,blank=True, null=True)  # GST of the vendor
    consignee_name = models.CharField(max_length=255)
    consignee_state_code = models.CharField(max_length=10,)  # Added
    remarks = models.CharField(max_length=255, blank=True, null=True)

    challan_number = models.CharField(max_length=50, blank=True, null=True)
    challan_date = models.DateField(blank=True, null=True)
    order_number = models.CharField(max_length=50, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)

    transport_mode = models.CharField(max_length=50, choices=TRANSPORT_MODES, blank=True, null=True)
    due_on = models.DateField(blank=True, null=True)
    payment_terms = models.CharField(max_length=50, blank=True, null=True)
    document = models.CharField(max_length=255, blank=True, null=True)
    delivery_terms = models.CharField(max_length=50, blank=True, null=True)
    transport = models.CharField(max_length=50, blank=True, null=True)
    place_of_supply = models.CharField(max_length=100, blank=True, null=True)
    l_r_number = models.CharField(max_length=50, blank=True, null=True)
    l_r_date = models.DateField(blank=True, null=True)
    ref = models.CharField(max_length=100, blank=True, null=True)

    # GST Percentages
    cgst_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sgst_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    igst_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    # GST Amounts
    cgst = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sgst = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    igst = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Discount
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    # Total Amount
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Banking Details
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_branch = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)

    date_supply = models.DateField(blank=True, null=True)
    time_supply = models.CharField(max_length=45, blank=True, null=True)
    
    description = models.CharField(max_length=255, default='Unknown')
    hsn_code = models.CharField(max_length=20, default='00000001')
    quantity = models.PositiveIntegerField(default=0)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
      # Discount
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    

    def calculate_totals(self):
        """Calculate total taxable value and GST amounts."""
        total_taxable_value = sum(item.total_value for item in self.items.all())
        
    
        # Apply Discount
        self.discount_amount = (total_taxable_value * self.discount_percentage) / 100
        taxable_after_discount = total_taxable_value - self.discount_amount

        if self.vendor.state_code and self.consignee_state_code:
            if self.vendor.state_code == self.consignee_state_code:
                self.cgst = (total_taxable_value * self.cgst_percentage) / 100
                self.sgst = (total_taxable_value * self.sgst_percentage) / 100
                self.igst = 0
            else:
                self.cgst = self.sgst = 0
                self.igst = (total_taxable_value * self.igst_percentage) / 100
        else:
            self.cgst = self.sgst = self.igst = 0  

       # Calculate Grand Total
        self.grand_total = taxable_after_discount + self.cgst + self.sgst + self.igst
        self.save(update_fields=['discount_amount', 'cgst', 'sgst', 'igst', 'grand_total'])

    def save(self, *args, **kwargs):
        
        total_before_discount = self.quantity * self.unit_rate
        self.discount_amount = (total_before_discount * self.discount_percentage) / 100
        self.total_value = total_before_discount - self.discount_amount
        if not self.invoice_number:
            last_invoice = Invoice.objects.order_by('-id').first()
            next_number = f"INV-{(last_invoice.id + 1) if last_invoice else 1:04d}"
            self.invoice_number = next_number
        super().save(*args, **kwargs)
        self.invoice.calculate_totals()
        
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.vendor.name if self.vendor else 'Unknown'}"

