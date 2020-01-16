# Generated by Django 3.0 on 2020-01-11 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devalappers', '0005_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField()),
                ('amount_paid', models.IntegerField()),
                ('outstanding', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devalappers.Customer')),
                ('invoice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devalappers.Invoice')),
            ],
            options={
                'unique_together': {('customer_id', 'invoice_no')},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devalappers.Customer')),
                ('invoice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devalappers.Invoice')),
            ],
            options={
                'unique_together': {('customer_id', 'invoice_no')},
            },
        ),
    ]