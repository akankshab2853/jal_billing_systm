# Generated by Django 5.1.6 on 2025-04-16 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_invoice', '0009_alter_billinvoice_cgst_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billinvoice',
            name='cgst',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='description',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='discount_percentage',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='grand_total',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='gst_rate',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='hsn_code',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='id',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='igst',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='price',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='sgst',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='total_value',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='vendor_address',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='vendor_code',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='vendor_gst_number',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='vendor_pan',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='vendor_phone_number',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='vendor_state',
        ),
        migrations.RemoveField(
            model_name='billinvoice',
            name='vendor_state_code',
        ),
        migrations.AddField(
            model_name='billinvoice',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='billinvoice',
            name='invoice_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='billinvoice',
            name='vendor_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterModelTable(
            name='billinvoice',
            table='billinvoice',
        ),
        migrations.AlterModelTable(
            name='vendor',
            table='vendor',
        ),
        migrations.DeleteModel(
            name='BillInvoiceItem',
        ),
    ]
