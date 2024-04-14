from django.urls import path
from .views import *

urlpatterns=[
    path('custumer/add/',CustumerAdd),
    path('custumerlist/',CustumerList),
    path('custumer/delete/<int:id>/',DeleteCustumer,name='custumer_delete'),
    path('custumer/update/<int:id>/',UpdateCustumer,name='custumer_update'),

    path('addorders/',OrdersAdd),
    path('orderslist/',OrdersList),
    path('deleteorder/<int:id>/',OrdersDelete,name='order_delete'),
    path('updateorder/<int:id>/',OrdersUpdate,name='order_update'),
    ]