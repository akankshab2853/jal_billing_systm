from django.db import models

class Itemstock(models.Model):
    description = models.CharField(unique=True, max_length=255)
    hsn_code = models.CharField(max_length=25, blank=True, null=True)
    stock_type = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.IntegerField()
    supplier = models.CharField(max_length=500, blank=True, null=True)
    def save(self, *args, **kwargs):   
        self.total_value = (self.quantity or 0) * (self.price or 0)
        super().save(*args, **kwargs)
 