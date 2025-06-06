# Generated by Django 5.1.6 on 2025-04-10 05:29

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_invoice', '0002_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(editable=False, max_length=50, unique=True)),
                ('invoice_date', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_code', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor_address', models.TextField(blank=True, null=True)),
                ('vendor_gst_number', models.CharField(blank=True, max_length=15, null=True)),
                ('vendor_pan', models.CharField(blank=True, max_length=15, null=True)),
                ('vendor_state', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor_state_code', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor_phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('consignee_name', models.CharField(blank=True, max_length=255, null=True)),
                ('consignee_state_code', models.CharField(max_length=10)),
                ('consignee_address', models.TextField(blank=True, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=50, null=True)),
                ('challan_number', models.CharField(blank=True, max_length=50, null=True)),
                ('challan_date', models.CharField(blank=True, max_length=50, null=True)),
                ('order_number', models.CharField(blank=True, max_length=50, null=True)),
                ('order_date', models.CharField(blank=True, max_length=50, null=True)),
                ('transport_mode', models.CharField(blank=True, choices=[('road', 'Road'), ('rail', 'Rail'), ('air', 'Air'), ('ship', 'Ship'), ('other', 'Other')], max_length=50, null=True)),
                ('veh_no', models.CharField(blank=True, max_length=50, null=True)),
                ('due_on', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_terms', models.CharField(blank=True, max_length=50, null=True)),
                ('document', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_terms', models.CharField(blank=True, max_length=50, null=True)),
                ('transport', models.CharField(blank=True, max_length=50, null=True)),
                ('time_of_supply', models.CharField(blank=True, max_length=50, null=True)),
                ('place_of_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('l_r_number', models.CharField(blank=True, max_length=50, null=True)),
                ('l_r_date', models.CharField(blank=True, max_length=50, null=True)),
                ('ref', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('igst', models.DecimalField(blank=True, choices=[(Decimal('0'), 0), (Decimal('2.5'), 2.5), (Decimal('5'), 5), (Decimal('9'), 9), (Decimal('12'), 12), (Decimal('18'), 18), (Decimal('24'), 24)], decimal_places=2, default=0, max_digits=10, null=True)),
                ('cgst', models.DecimalField(blank=True, choices=[(Decimal('0'), 0), (Decimal('2.5'), 2.5), (Decimal('5'), 5), (Decimal('9'), 9), (Decimal('12'), 12), (Decimal('18'), 18), (Decimal('24'), 24)], decimal_places=2, default=0, max_digits=10, null=True)),
                ('sgst', models.DecimalField(blank=True, choices=[(Decimal('0'), 0), (Decimal('2.5'), 2.5), (Decimal('5'), 5), (Decimal('9'), 9), (Decimal('12'), 12), (Decimal('18'), 18), (Decimal('24'), 24)], decimal_places=2, default=0, max_digits=10, null=True)),
                ('gst_rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('description_name', models.CharField(blank=True, max_length=255, null=True)),
                ('hsn_code', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('discount_percentage', models.IntegerField(default=0)),
                ('total_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='InvoiceItem',
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={},
        ),
    ]
