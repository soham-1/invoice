from django.db import models

# Create your models here.



class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=150)
    outstanding = models.IntegerField()

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    date = models.DateField()
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    invoice_pic = models.ImageField(upload_to='invoice/images',default="Not present")
    invoice_desc = models.CharField(max_length=500,default='')