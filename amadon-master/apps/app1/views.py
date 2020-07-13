from django.shortcuts import render, redirect
from .models import Order, Product
# from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def buy_product(request):
    if request.method == 'POST':
        this_product = Product.objects.filter(id=request.POST['id']) # returning list ob objects
        if not this_product: # here we covering situation if user press buy, without selecting any product (in general).
            return redirect('/')
        else:
            quantity = int(request.POST["quantity"])
            total_price = quantity*(float(this_product[0].price)) # first object from the list
            Order.objects.create(quantity_ordered=quantity, total_price=total_price)
            return redirect('/checkout')
    else:
        return redirect('/') 



def checkout(request):
    last = Order.objects.last()
    price=last.total_price
    # full_order = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    # full_price = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    all_orders = Order.objects.all()
    order_sum = 0
    qty = 0
    for order in all_orders:
        order_sum += order.total_price
        qty += order.quantity_ordered


    order_sum = round(order_sum, 2)
    context = {
        'orders':qty,
        'total':order_sum,
        'bill':price,
    }
    return render(request, "store/checkout.html",context)
































