from django.db import models

class product(models.Model):
    p_name=models.CharField(max_length=200,null=True)
    p_code=models.CharField(max_length=200,null=True)
    p_price=models.FloatField(default=0)
    gst=models.IntegerField(default=0)

    def __str__(self):
        return self.p_name