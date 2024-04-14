from django.shortcuts import render,redirect
from .forms import *
from .models import *

def CustumerList(request):
    context ={
        "custumerList":Custumer.objects.all()
    }
    return render(request,'custumers.html',context)

def CustumerAdd(request):
    context ={
        'custumer_form':Custumer_Form()
    }
    if request.method == "POST":
        custumer_form = Custumer_Form(request.POST)        
        if custumer_form.is_valid():
            custumer_form.save()
    return render(request,'custumer_add.html',context)

def DeleteCustumer(request,id):
    selected_custumer= Custumer.objects.get(id=id)
    selected_custumer.delete()
    return redirect('/inventory/custumer/')

def UpdateCustumer(request,id):
    selected_custumer= Custumer.objects.get(id=id)
    context ={
        'custumer_form':Custumer_Form(instance=selected_custumer)
    }
    if request.method=='POST':
        custumer_form=Custumer_Form(request.POST,instance=selected_custumer)
        if custumer_form.is_valid():
            custumer_form.save()
        return redirect('/inventory/custumer/')

    return render(request,'custumer_add.html',context)

def OrdersAdd(request):
    context ={
        "order_form":Orders_Form()
    }
    if request.method == 'POST':
        # order_form = Orders_Form(request.POST)  
        selected_product= product.objects.get(id=request.POST['p_reference'])
        amount=float(selected_product.p_price)*float(request.POST['quantity'])
        gst_amt=(amount*selected_product.gst)/100
        bill_amt=amount+gst_amt
        new_order=Orders(c_reference_id=request.POST['c_reference'],
                         p_reference_id=request.POST['p_reference'],
                         o_number=request.POST['o_number'],
                         o_date=request.POST['o_date'],
                         quantity=request.POST['quantity'],
                         amount=amount,
                         gst_amt=gst_amt,
                         bill_amt=bill_amt)
        new_order.save()
        return redirect('/orders/orderslist/')
    return render(request,'orders_add.html',context)

def OrdersList(request):
    context={
         'all_orders':Orders.objects.all()
    }
    return render(request,'orders.html',context)
    
def OrdersDelete(request,id):
    order=Orders.objects.get(id=id)
    order.delete()
    return redirect('/orders/orderslist/')

def OrdersUpdate(request,id):
    order=Orders.objects.get(id=id)
    context={
        'order_form':Orders_Form(instance=order)
    }
    if request.method == 'POST':
        selected_product= product.objects.get(id=request.POST['p_reference'])
        amount=float(selected_product.p_price)*float(request.POST['quantity'])
        gst_amt=(amount*selected_product.gst)/100
        bill_amt=amount+gst_amt
        order_filter=Orders.objects.filter(id=id)
        order_filter.update(c_reference_id=request.POST['c_reference'],
                         p_reference_id=request.POST['p_reference'],
                         o_number=request.POST['o_number'],
                         o_date=request.POST['o_date'],
                         quantity=request.POST['quantity'],
                         amount=amount,
                         gst_amt=gst_amt,
                         bill_amt=bill_amt)
        return redirect('/orders/orderslist/')
    
    return render(request,'orders_add.html',context)
