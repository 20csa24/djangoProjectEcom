from django.db import models
from Inventory.models import *
class Custumer(models.Model):
    c_name=models.CharField(max_length=200,null=True)
    c_since=models.DateField(null=True)

    def __str__(self):
        return self.c_name

class Orders(models.Model):
    c_reference=models.ForeignKey(Custumer,on_delete=models.CASCADE,null=True)
    p_reference=models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    o_number=models.CharField(max_length=20,null=True)
    o_date=models.DateField(null=True)
    quantity=models.FloatField(default=0)
    amount=models.FloatField(default=0)
    gst_amt=models.FloatField(default=0)
    bill_amt=models.FloatField(default=0)

    def __str__(self):
        return self.o_number 

