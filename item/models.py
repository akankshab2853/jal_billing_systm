from django.db import models

class Stock(models.Model):
    STOCK_TYPE_CHOICES = [
        ('parent', 'Parent'),
        ('child', 'Child'),
    ]
    
    name = models.CharField(max_length=255, unique=True)
    hsn_code = models.CharField(max_length=25, verbose_name="HSN Code")
    stock_type = models.CharField(max_length=10, choices=STOCK_TYPE_CHOICES, default='Parent')
    quantity = models.PositiveIntegerField()  # Total stock available
    price = models.IntegerField()  # Price per unit
    supplier = models.CharField(max_length=500)
       
    def save(self, *args, **kwargs):   
        self.total_value = self.quantity * self.price
        super().save(*args, **kwargs)
       
    def __str__(self):
        return f"{self.name} ({self.get_stock_type_display()}) - {self.quantity} units"
