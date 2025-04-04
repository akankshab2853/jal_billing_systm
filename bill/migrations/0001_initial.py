# Generated by Django 5.1.6 on 2025-03-24 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price_per_piece', models.PositiveIntegerField()),
                ('gst', models.PositiveIntegerField(help_text='GST percentage')),
                ('total_price', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'db_table': 'bill',
                'managed': True,
            },
        ),
    ]
