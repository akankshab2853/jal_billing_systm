from django.db import models

class Bill(models.Model):  
    id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField() 
    price_per_piece = models.PositiveIntegerField()
    gst = models.PositiveIntegerField(help_text="GST percentage")  
    total_price = models.PositiveIntegerField(editable=False) 

    class Meta:
        db_table = 'bill'  
        managed = True  

    def save(self, *args, **kwargs):
        """Calculate total price and apply GST before saving."""
        self.total_price = self.quantity * self.price_per_piece
        gst_amount = (self.total_price * self.gst) / 100
        self.total_price += gst_amount  

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item_name} - {self.quantity} items - ₹{self.total_price} (incl. GST)"
