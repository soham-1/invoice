# Generated by Django 3.0 on 2020-01-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devalappers', '0002_invoice_invoice_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='outstanding',
            field=models.IntegerField(),
        ),
    ]