# Generated by Django 5.1.6 on 2025-04-01 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill_invoice', '0002_supplier'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={},
        ),
        migrations.AlterModelOptions(
            name='invoiceitem',
            options={},
        ),
    ]
