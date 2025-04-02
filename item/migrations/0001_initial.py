# Generated by Django 5.1.6 on 2025-03-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('hsn_code', models.CharField(max_length=25, verbose_name='HSN Code')),
                ('stock_type', models.CharField(choices=[('parent', 'Parent'), ('child', 'Child')], default='Parent', max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.IntegerField()),
                ('supplier', models.CharField(max_length=500)),
            ],
        ),
    ]
