from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import *
from django.contrib.auth.models import User
import json
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

def index(request):
    return render(request,'index.html')

def temp(request):
    return render(request,'temp.html')


def about(request):
    return render(request,'about.html')

def cart2(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
    context = {'items': items,'order':order}
    return render(request,'cart2.html', context)

# class checkout(ListView):
#     model = OrderItem
#     template_name = 'cart.html'

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0}
    context = {'items': items,'order':order}
    return render(request,'cart.html', context)


class collectionv(ListView):
    model=gamedata
    # add detail view for posts
    template_name = 'collection.html'

    # def forcart(request):
    #     if request.user.is_authenticated:
    #         customer = request.user.customer
    #         order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #         items = order.orderitem_set.all()
    #         cartitems = order.get_cart_items
    #     else:
    #         items = []
    #         order = {'get_cart_total': 0,'get_cart_items': 0}
    #         cartitems = order['get_cart_items']
    #
    #     context = {'cartitems':cartitems}
    #     return render(request, 'collection.html',context)


def updateitem(request):
    data = json.loads(request.body)

    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('productId:',productId)

    customer =request.user.customer
    product = gamedata.objects.get(id=productId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity-1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)
