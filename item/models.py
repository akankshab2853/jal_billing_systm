from ast import arg
from django.db import models

class Itemstock(models.Model):
    description = models.CharField(unique=True, max_length=255)
    hsn_code = models.CharField(max_length=25, blank=True, null=True)
    stock_type = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.IntegerField()
    supplier = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemstock'
        
        
class Defectivestock(models.Model):
    stock = models.CharField(max_length=255, blank=True, null=True)
    stock_type = models.CharField(max_length=100, blank=True, null=True)
    defective_quantity = models.IntegerField()
    reusable_quantity = models.IntegerField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        reusable = self.reusable_quantity or 0
        non_reusable_quantity = self.defective_quantity - reusable

        try:
            item = Itemstock.objects.get(description=self.stock)

            if item.quantity is not None:
                item.quantity = item.quantity - non_reusable_quantity
                item.save()
        except Itemstock.DoesNotExist:
            pass

        super()#.save(*args, **kwargs)
    class Meta:
        managed = False
        db_table = 'defectivestock'