# Generated by Django 5.1.6 on 2025-04-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='bank_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='ifsc_code',
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
