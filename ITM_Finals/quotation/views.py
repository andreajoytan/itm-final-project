from django.shortcuts import render, redirect

from django.http import JsonResponse
import json
import datetime
from .models import *
from .forms import *

def my_orders(request):
    my_orders=Order.objects.filter(customer = Customer.objects.get(email=request.user.email)).order_by('-id')
    return render(request, 'quotation/my_orders.html',{
        'my_orders':my_orders,
        })

def my_orders_items(request, id):
    order=Order.objects.get(id=id)
    orders_items=OrderItem.objects.filter(order=order).order_by('-id')
    return render(request, 'quotation/my_orders_items.html',{
        'orders_items':orders_items,
        })

def process_order (request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = Customer.objects.get(email=request.user.email)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

    else:
        print('Please log in first before proceeding.') 
    return JsonResponse('Transaction completed.', safe=False)

def cart(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(email=request.user.email)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    return render(request, 'quotation/cart.html', {
        'items': items,
        'order': order,
        'products':products,
        'cartItems' :cartItems
    })

def checkout(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(email=request.user.email)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.OrderItem_set.all()
        cartItems = order.get_cart_items
    
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    return render(request, 'store/checkout.html', {
        'items' : items, 
        'order' : order,
        'cartItems' :cartItems
    }) 

def updateItem(request):
    data = json.loads(request.body) 
    productId = data['productId']   
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = customer = Customer.objects.get(email=request.user.email)
    print('Customer:', customer)

    product = Product.objects.get(id=productId) 
    print('Product:', product)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    print('Order:', order, 'Created:', created)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product) 
    print('OrderItem:', orderItem, 'Created:', created)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    print('OrderItem quantity:', orderItem.quantity)

    if orderItem.quantity <= 0:
        orderItem.delete()
        print('OrderItem deleted')

    return JsonResponse('Item was added', safe=False)

