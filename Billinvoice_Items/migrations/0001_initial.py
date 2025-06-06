# Generated by Django 5.1.6 on 2025-04-16 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bill_invoice', '0010_remove_billinvoice_cgst_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billinvoiceitems',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('hsn_code', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('unit_rate', models.FloatField(blank=True, null=True)),
                ('discount_percentage', models.FloatField(blank=True, null=True)),
                ('gst_rate', models.FloatField(blank=True, null=True)),
                ('cgst', models.FloatField(blank=True, null=True)),
                ('sgst', models.FloatField(blank=True, null=True)),
                ('igst', models.FloatField(blank=True, null=True)),
                ('total_value', models.FloatField(blank=True, null=True)),
                ('discount_amount', models.FloatField(blank=True, null=True)),
                ('grand_total', models.FloatField(blank=True, null=True)),
                ('invoice_number', models.ForeignKey(db_column='invoice_number', on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='bill_invoice.billinvoice')),
            ],
            options={
                'db_table': 'billinvoiceitems',
            },
        ),
    ]
