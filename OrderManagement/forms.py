from django.forms import ModelForm
from .models import *

class Custumer_Form(ModelForm):
    class Meta:
        model = Custumer
        fields ='__all__'

class Orders_Form(ModelForm):
    class Meta:
        model=Orders
        fields=['c_reference','p_reference','o_number','o_date','quantity',]